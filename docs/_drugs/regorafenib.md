---
layout: default
title: Regorafenib
parent: 高證據等級 (L1-L2)
nav_order: 639
evidence_level: L2
indication_count: 10
---

# Regorafenib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Regorafenib：從轉移性大腸直腸癌到脂肪肉瘤

## 一句話總結

Regorafenib 是一種多重酪胺酸激酶抑制劑，國際上核准用於轉移性大腸直腸癌、腸胃道基質瘤（GIST）與肝細胞癌，但**目前未在香港上市**。TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，目前有 **2 個已完成的 Phase 2 臨床試驗**和 **9 篇文獻**涉及此適應症——但須注意，其中關鍵試驗的脂肪肉瘤亞組結果實際上是**陰性**的，詳見下文。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可證資料；據國際文獻，原廠核准適應症為轉移性大腸直腸癌、GIST、肝細胞癌 |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（需嚴格解讀，見結論） |

---

## 為什麼這個預測合理？

Regorafenib 是口服多重激酶抑制劑，標靶血管新生相關受體（VEGFR1-3、TIE2）、間質受體（PDGFR-β、FGFR）及致癌相關受體酪胺酸激酶（KIT、RET、RAF）。它是第一個在轉移性大腸直腸癌標準治療失敗後展現存活效益的小分子多激酶抑制劑，於 2012 年獲國際藥證核准，其後也擴展至 GIST 與肝細胞癌。

軟組織肉瘤（含脂肪肉瘤）在腫瘤生物學上同樣高度依賴血管新生與間質訊號傳遞，這是 TxGNN 預測脂肪肉瘤的機轉基礎——同類機轉藥物 pazopanib（VEGFR 抑制劑）已核准用於軟組織肉瘤。

然而，機轉合理≠療效已證實。REGOSARC 試驗（NCT01900743）依組織型分層分析顯示，regorafenib 對平滑肌肉瘤、滑膜肉瘤等**非脂肪性**肉瘤有效，但**對脂肪肉瘤未見效益**；SARC024 試驗的脂肪肉瘤世代（PMID 32701199）進一步證實「不支持將 regorafenib 常規用於此族群」。換言之，血管新生機轉在脂肪肉瘤中可能被其他驅動路徑（如 MDM2/CDK4 擴增）掩蓋，導致單藥療效不彰。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | 完成 | 219 | REGOSARC：法奧德三國隨機雙盲安慰劑對照試驗，評估 regorafenib 於蒽環類治療失敗後轉移性軟組織肉瘤（含脂肪肉瘤世代）之療效與安全性 |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 完成 | 131 | SARC024：口服 regorafenib 於特定肉瘤亞型（含脂肪肉瘤）之 blanket protocol 試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncol | REGOSARC 主報告：regorafenib 於蒽環類治療後轉移性軟組織肉瘤之安全性與療效評估 |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 脂肪肉瘤世代：regorafenib 對照安慰劑，結果**不支持**常規用於治療難治性脂肪肉瘤 |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT（交叉後分析） | Eur J Cancer | REGOSARC 更新分析：regorafenib 對平滑肌肉瘤、滑膜肉瘤等有效，但**對脂肪肉瘤無效** |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | RCT Protocol | BMC Cancer | REGOSARC 試驗設計：血管新生訊號於肉瘤生物學中的關鍵角色 |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT 次分析（QoL） | Cancer | REGOSARC 之 Q-TWiST 分析：regorafenib 改善無症狀進展存活時間 |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | 回顧 regorafenib 於各類肉瘤（含脂肪肉瘤、GIST）治療角色之演變 |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Crit Rev Oncol Hematol | 進展期軟組織肉瘤一線治療後之維持療法回顧 |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | 回顧性研究（非 regorafenib） | Anticancer Drugs | Anlotinib（非 regorafenib）於脂肪肉瘤之療效，僅供 TKI 類別效應參考 |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | 病例報告（非 regorafenib） | Rare Tumors | Pazopanib（非 regorafenib）於尤文氏肉瘤之個案，僅供機轉類比參考 |

---

## 香港上市資訊

目前查無香港許可證登記（`market_status: 未上市`，許可證數 0），regorafenib 尚未在香港取得任何藥品註冊。

---

## 細胞毒性

Regorafenib 屬抗腫瘤藥物（多重酪胺酸激酶抑制劑），故列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重酪胺酸激酶抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 資料有限；文獻主要記載皮膚、肝臟及心血管毒性，非典型骨髓抑制表現，建議常規監測 |
| 致吐性分級 | 低（口服 TKI 類別一般屬低致吐性） |
| 監測項目 | 肝功能（AST/ALT/bilirubin）、血壓、皮膚（手足皮膚反應）、CBC |
| 處置防護 | 口服標靶藥物，不需傳統細胞毒性藥物之特殊配置防護，但建議依機構標準作業程序處理 |

（骨髓抑制/毒性描述參考 PMID 23700287〔手足皮膚反應統合分析〕、23981115〔肝毒性統合分析〕、36583425〔血壓上升〕、38761350〔TKI 毒性系統性回顧〕。）

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
脂肪肉瘤此一適應症有 2 個已完成的 Phase 2 RCT 支撐（達 L2 證據等級），但**須特別注意**：REGOSARC 與 SARC024 兩項試驗的脂肪肉瘤亞組分析均為陰性結果，regorafenib 單藥對此適應症未展現顯著療效。因此「Proceed with Guardrails」意指僅適合在臨床試驗或合併治療研究框架下探索，**不建議常規單藥使用**於脂肪肉瘤患者。

**若要推進需要：**
- TFDA/香港仿單警語與禁忌資料（DG001，Blocking 級缺口，目前無法進入安全性初評）
- 完整作用機轉資料來源確認（DG002）
- 針對脂肪肉瘤的合併治療（如免疫治療、化療併用）後續試驗數據，以釐清單藥無效後的替代策略
- 香港藥品上市/許可證申請評估（目前完全未上市，無本地安全性與可近性資料）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

