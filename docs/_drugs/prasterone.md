---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 5
---

# Prasterone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# PRASTERONE：原適應症資料缺失，TxGNN 預測肝素輔因子 II 缺乏症

## 一句話總結

本評估包中並未提供 PRASTERONE 的原適應症與作用機轉資料（DrugBank 查詢結果為空）。TxGNN 模型針對此藥物給出 5 個高分預測適應症，評分最高者為**肝素輔因子 II 缺乏症 (Heparin Cofactor II Deficiency)**，預測分數高達 **99.99%**，但目前**沒有任何臨床試驗或文獻**支持這個方向。其餘候選中僅 1 項有文獻佐證，且該文獻方向與「治療」假設相反，需特別留意。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肝素輔因子 II 缺乏症 (Heparin Cofactor II Deficiency) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅模型預測，無臨床或文獻佐證） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

> 註：原適應症欄位因本評估包未提供資料而省略（DrugBank 查詢無 `original_indications` 與 `original_moa` 資料）。

---

## 為什麼這個預測合理？

目前缺乏 PRASTERONE 的作用機轉（MOA）與原適應症資料，DrugBank 查詢結果為空值，此為本評估的 Blocking 等級資料缺口（DG002）。根據 TxGNN 提供的推理說明，肝素輔因子 II 缺乏症是一種罕見的先天性凝血抑制因子缺乏疾病；PRASTERONE 作為雄性素前驅物，目前沒有已知機轉可解釋其如何調節 heparin cofactor II 的表現或活性。

評估團隊研判，此高分預測（99.99%）很可能源自知識圖譜中「血栓傾向 (thrombophilia)」相關節點的鄰近嵌入相似性（即 *guilt-by-association* 效應），而非真實的藥理連結。這個推論同樣適用於本次另外 4 個排名相近的候選適應症——它們高度聚集於凝血相關疾病家族，顯示可能是圖譜結構性偏差造成的系統性高分群集，而非個別藥理訊號。

### 其他預測適應症與重要安全性訊號

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 說明 |
|------|------|-----------|---------|------|
| 2 | Factor V 過量合併自發性血栓症 | 99.98% | L5 | 無文獻或試驗支持，純模型預測 |
| 3 | 第二型抗凝血酶缺乏症 | 99.98% | L5 | 無文獻或試驗支持，純模型預測 |
| 4 | 血栓傾向 (Thrombophilia) | 99.91% | L4 | ⚠️ 4 篇文獻描述**雄性素過高與血栓風險「增加」相關**，方向與治療假設相反，應視為安全性警訊而非再利用機會 |
| 5 | 嚴重非增殖性糖尿病視網膜病變 | 99.25% | L5 | 無文獻或試驗支持，純屬理論推測（DHEA 抗氧化特性的間接聯想） |

**血栓傾向 (Thrombophilia) 相關文獻（僅供安全性參考，非療效證據）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23683262](https://pubmed.ncbi.nlm.nih.gov/23683262/) | 2013 | Cohort/Correlational | J Chin Med Assoc | PCOS 患者血栓傾向與復發性流產相關性升高 |
| [25531921](https://pubmed.ncbi.nlm.nih.gov/25531921/) | 2015 | Guideline/Review | Hum Fertil | IVF 輔助療法實證回顧，未特別支持雄性素用於治療血栓傾向 |
| [24152686](https://pubmed.ncbi.nlm.nih.gov/24152686/) | 2014 | Case Report | J Clin Endocrinol Metab | 卵巢萊氏細胞瘤導致極端雄性素過高，併發紅血球增多症與反覆肺栓塞 |
| [6241118](https://pubmed.ncbi.nlm.nih.gov/6241118/) | 1984 | Review | Clin Obstet Gynecol | 妊娠高血壓病理生理學回顧（間接關聯） |

---

## 臨床試驗證據（肝素輔因子 II 缺乏症）

目前無相關臨床試驗登記。

---

## 文獻證據（肝素輔因子 II 缺乏症）

目前無相關文獻。

---

## 香港上市資訊

PRASTERONE 目前於香港**未上市**，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單（本評估包中 `key_warnings`、`contraindications`、DDI 查詢均無資料）。

- 文獻回顧顯示雄性素過高與血栓傾向風險增加有關聯（見上方「其他預測適應症」說明），實際評估或處方前應審慎考量病患的凝血相關病史，此為文獻觀察而非正式禁忌症資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個預測適應症中，4 個為 L5（僅模型預測，無任何臨床或文獻資料），且高度集中於罕見凝血因子疾病家族，懷疑為知識圖譜嵌入偏差（guilt-by-association）而非真實藥理訊號。
- 唯一有文獻佐證的候選（血栓傾向）方向與治療假設相反——現有證據顯示雄性素過高可能「增加」而非降低血栓風險，此為安全性警訊而非再利用機會。
- 原適應症與作用機轉資料完全缺失（Blocking 資料缺口），且香港未上市，無法進行安全性初評（S1）。

**若要推進需要：**
- 補齊作用機轉、原適應症、仿單警語與禁忌症資料（DG001 為 Blocking、DG002 為 High 等級缺口，需優先解決）
- 釐清 PRASTERONE／DHEA 對凝血系統的實際藥理效應方向（促進或抑制），才能判斷血栓傾向候選究竟是風險還是機會
- 若仍評估肝素輔因子 II 缺乏症等罕見適應症，需先取得任何前臨床或病例層級證據；目前完全空白，暫不建議投入進一步資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

