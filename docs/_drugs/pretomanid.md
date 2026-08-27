---
layout: default
title: Pretomanid
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 10
---

# Pretomanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Pretomanid：從抗藥性肺結核到念珠菌病

## 一句話總結

Pretomanid 是治療多重抗藥性/廣泛抗藥性肺結核（MDR/XDR-TB）BPaL、BPaLM 方案的核心成分之一。
TxGNN 模型預測它可能對**念珠菌病 (Candidiasis)** 有效，預測分數高達 **99.69%**，
但目前**完全沒有臨床試驗或文獻**支持這個方向，機轉上也找不到合理連結，屬於純模型預測的假設。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 抗藥性肺結核（MDR/XDR-TB，BPaL/BPaLM 方案，見文獻證據） |
| 預測新適應症 | 念珠菌病 (Candidiasis) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

> 註：`taiwan_regulatory.licenses` 為空，故「原適應症」欄位無法從許可證資料取得，以上內容係根據文獻證據中反覆提及之核准用途（BPaL 方案治療 XDR/MDR 肺結核）整理，非正式許可證登記資料。

---

## 為什麼這個預測合理？

Pretomanid 的正式 MOA 資料標記為缺失（[Data Gap]），但根據文獻證據可還原其已知機轉：Pretomanid 屬於 nitroimidazooxazine（硝基咪唑氧氮呯）類藥物，其抗菌活性依賴**分枝桿菌專一**的 Ddn（deazaflavin-dependent nitroreductase）酶系統將前驅藥活化，產生活性代謝物抑制分枝菌酸（mycolic acid）合成並釋放活性氮物種毒殺菌體。

念珠菌病是真菌感染，其致病與治療標靶（如麥角固醇合成路徑、細胞壁 β-glucan 等）與分枝桿菌的細胞壁/呼吸鏈系統完全不同。根據本評估的機轉分析：「無已知抗真菌機轉；pretomanid 之硝基還原酶活化機制專一於分枝桿菌 Ddn 酶系統，與念珠菌之細胞壁/麥角固醇合成路徑無重疊」，兩者在藥理上**沒有重疊基礎**。

TxGNN 給出 99.69% 高分，較可能反映知識圖譜中「感染症」節點類別的嵌入相似性（embedding artifact），而非真實生物學訊號 —— 這與同一藥物其他高分預測（如 leprosy、HIV，詳見結論）呈現的模式一致：分數高，但深入查證後多為資料誤配或反向（否定）證據。因此這個預測目前**不具機轉合理性**，僅能視為探索性假設。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

補充：根據本評估對其他預測適應症的機轉分析文字，Pretomanid 已知存在 **QT 間期延長**之心臟安全性疑慮（尤其與 bedaquiline 併用時），此為既有藥物警語提示，非正式安全性資料來源，僅供臨床參考。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測適應症（念珠菌病）證據等級為 L5，無任何臨床試驗或文獻支持，機轉分析亦顯示與原藥理機轉無重疊，純屬 TxGNN 嵌入相似性預測。
- 檢視本藥物其他高分預測（leprosy、HIV infectious disease，皆為 L4）發現查證後皆非真正支持性訊號：leprosy 有直接體外證據（PMID 17005816）顯示 *M. leprae* 對本藥天然抗藥；HIV 相關試驗與文獻實為 HIV/TB 共感染族群中以 BPaL/BPaLM 治療「結核病」之研究，並非證明本藥對 HIV 本身療效。此模式顯示 TxGNN 對本藥物的預測品質可能系統性偏低，反映 Mycobacterium／感染症節點的結構相似性造成的嵌入偽陽性，而非真實老藥新用訊號。
- 存在 Blocking 等級資料缺口（DG001：TFDA 仿單警語/禁忌資料缺失），目前無法進入 S1 安全性初評；MOA 資料亦缺失（DG002，High），影響機轉關聯性分析的完整性。

**若要推進需要：**
- 補齊 TFDA 仿單警語/禁忌資料（DG001），以完成 S1 安全性初評
- 取得完整 DrugBank MOA 資料（DG002），強化機轉關聯性分析
- 針對候選適應症進行體外/動物機轉驗證，排除知識圖譜嵌入偽陽性的可能性
- 若欲重新篩選候選適應症，建議優先評估機轉上較具理論基礎者（如 Bacteroidaceae 厭氧菌感染，其硝基咪唑類前驅藥活化機制與同類藥物 metronidazole 存在理論重疊），並補充體外藥敏測試資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

