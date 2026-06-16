---
layout: default
title: Eribulin
parent: 高證據等級 (L1-L2)
nav_order: 280
evidence_level: L2
indication_count: 10
---

# Eribulin
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

# Eribulin：從脂肪肉瘤到纖維母細胞腫瘤

## 一句話總結

Eribulin 是一種微管抑制劑，已獲 FDA 核准用於不可切除或轉移性脂肪肉瘤及晚期乳癌，台灣目前尚未上市。
TxGNN 模型對 10 個新適應症進行預測，其中**纖維母細胞腫瘤 (Fibroblastic Neoplasm)** 為唯一達到 L2 證據等級者，
有 **1 個已完成的 Phase 2 臨床試驗**及 **8 篇文獻**支持，建議「Proceed with Guardrails」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 脂肪肉瘤（FDA 核准）；台灣未上市 |
| 最佳預測新適應症 | 纖維母細胞腫瘤 (Fibroblastic Neoplasm) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L2 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 10 個預測適應症總覽

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|------|-----------|---------|---------|
| 1 | 常染色體隱性家族性地中海熱 (Familial Mediterranean Fever) | 99.82% | L5 | Hold |
| 2 | 隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma Protuberans) | 99.66% | L4 | Hold |
| 3 | 胸膜間皮瘤 (Pleural Mesothelioma) | 99.51% | L5 | Hold |
| 4 | 惡性腹膜間皮瘤 (Malignant Peritoneal Mesothelioma) | 99.47% | L5 | Hold |
| 5 | 卵巢黏液樣脂肪肉瘤 (Ovarian Myxoid Liposarcoma) | 99.47% | L4 | Research Question |
| 6 | 胸膜腺瘤樣腫瘤 (Pleural Adenomatoid Tumor) | 99.46% | L5 | Hold |
| 7 | 胸膜雙相型間皮瘤 (Pleural Biphasic Mesothelioma) | 99.37% | L5 | Hold |
| **8** | **纖維母細胞腫瘤 (Fibroblastic Neoplasm)** | **99.36%** | **L2** | **Proceed with Guardrails** |
| 9 | 胸膜上皮樣間皮瘤 (Pleural Epithelioid Mesothelioma) | 99.35% | L5 | Hold |
| 10 | 心臟纖維肉瘤 (Heart Fibrosarcoma) | 99.35% | L5 | Hold |

> **焦點說明**：本報告詳細分析以 **纖維母細胞腫瘤（排名第 8）** 為主，因其為 10 個預測中唯一具備 Phase 2 直接臨床試驗的適應症，實際可行動性最高。排名第 1 的家族性地中海熱（FMF）雖 TxGNN 分數最高，但機轉評估認為此為模式偽陽性，不建議推進。

---

## 為什麼這個預測合理？

Eribulin（品牌名：Halaven）是天然化合物海兔毒素 B（halichondrin B）的合成類似物。其作用機轉為選擇性結合微管 plus 端，抑制微管聚合與動態不穩定性，最終引起 G2/M 期細胞週期阻滯並誘導凋亡。此外，eribulin 在腫瘤微環境中具有抗血管新生及逆轉上皮—間質轉化（EMT）的附加效應，對富含纖維間質的腫瘤尤具意義。

纖維母細胞腫瘤（Fibroblastic Neoplasm）是源自纖維母細胞的一大類軟組織腫瘤，涵蓋孤立性纖維瘤（SFT）、纖維肉瘤（FS）、黏液纖維肉瘤（MFS）等亞型。這些腫瘤的共同特徵是對 doxorubicin 等標準化療抵抗性高，且手術切除後復發率不低。Eribulin 已獲 FDA 核准用於脂肪肉瘤（同屬軟組織肉瘤），機轉上的類比性使此預測具生物學合理性。

孤立性纖維瘤（SFT）的主要驅動突變為 NAB2-STAT6 融合基因，對標準化療反應有限，正是需要不同作用機轉藥物介入的情境。多項前臨床研究已記錄 eribulin 對纖維肉瘤細胞株及 SFT PDX 模型的體外/體內活性，轉譯基礎相對充分，且已有完成的 Phase 2 試驗（ERASING）提供直接臨床依據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Phase 2 | 已完成 | 16 | ERASING 試驗（義大利肉瘤組）：直接評估 eribulin 用於進展期孤立性纖維瘤（SFT）；SFT 屬纖維母細胞腫瘤範疇，為目前最強直接臨床依據；樣本數小（n=16）為主要限制，完整結果論文發表狀態待確認 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | 前臨床（PDX 模型） | Eur J Cancer | SFT 患者衍生異種移植模型預測 doxorubicin/dacarbazine 有效（已獲臨床驗證），同時顯示 trabectedin 或 eribulin 具潛在療效 |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | 前臨床（體外） | Anticancer Research | 重組甲硫氨酸酶（rMETase）與 eribulin 對纖維肉瘤細胞具廣泛協同效應，而對正常纖維母細胞毒性低，顯示腫瘤選擇性 |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | 前臨床（體外） | Anticancer Research | rMETase 可使高度 eribulin 抗藥性纖維肉瘤細胞（HT1080）敏感度提升 16 倍，提供克服抗藥性的新策略 |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | 前臨床（體外/體內） | In Vivo | 超抗藥性纖維肉瘤細胞惡性度升高，但在裸鼠模型中可藉甲硫氨酸限制 + eribulin 協同清除，強化轉譯依據 |
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Review | Cancers | 腦膜外 SFT 診斷與治療現況回顧；涵蓋分子病理（NAB2-STAT6）、治療選項及 eribulin 等新藥潛力 |
| [39625530](https://pubmed.ncbi.nlm.nih.gov/39625530/) | 2024 | 前臨床（細胞株建立） | Human Cell | 黏液纖維肉瘤新細胞株 SMU-MFS 建立，提供研究 eribulin 等新治療方案的工具 |
| [34383271](https://pubmed.ncbi.nlm.nih.gov/34383271/) | 2021 | 前臨床（細胞株建立） | Human Cell | NCC-MFS4-C1 黏液纖維肉瘤新細胞株建立，擴充此亞型研究資源，有助於評估 eribulin 的 MFS 適用性 |
| [35906852](https://pubmed.ncbi.nlm.nih.gov/35906852/) | 2023 | 個案報告 | Genes Chromosomes Cancer | MPNST 患者攜帶 SNRNP70-NTRK3 融合基因對 entrectinib 戲劇性反應；間接說明纖維母細胞源性肉瘤的分子靶向治療潛力 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（微管抑制劑，Halichondrin B 合成類似物） |
| 骨髓抑制風險 | 高（Grade 3/4 嗜中性白血球減少症為主要劑量限制毒性，需監測感染徵象） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類計數）、肝腎功能、周邊神經學評估（感覺/運動神經病變）、QTc 間期 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；靜脈注射製劑需依廠商建議稀釋與給藥速率執行 |

---

## 安全性考量

安全性資訊請參考原廠仿單（台灣未上市，建議參閱 FDA/EMA 核准仿單）。

已知主要安全考量（基於 FDA 核准藥品資訊，TFDA 仿單資料待補齊）：

- **骨髓毒性**：嗜中性白血球減少症為最常見 Grade 3/4 不良反應，需定期監測血球並評估感染風險
- **周邊神經病變**：用藥前及用藥期間需定期神經學評估，一旦出現 Grade 2 以上需考慮劑量調整
- **QT 間期延長**：建議用藥前及過程中監測心電圖，合併使用 QT 延長藥物時需特別謹慎
- **肝腎功能異常**：中度肝功能或腎功能受損者需調整劑量，嚴重損傷者禁用

---

## 結論與下一步

**決策：Proceed with Guardrails（針對纖維母細胞腫瘤）**

**理由：**
Phase 2 ERASING 試驗（NCT03840772）已完成，直接評估 eribulin 於孤立性纖維瘤（SFT，屬纖維母細胞腫瘤）的療效，加上多項前臨床研究（PDX 模型、纖維肉瘤細胞株）支持其機轉合理性，達到 L2 證據等級。作用機轉與此類腫瘤生物學高度吻合，且 FDA 已核准 eribulin 於軟組織肉瘤，類比依據充分。

**若要推進需要：**
- **最優先**：取得 ERASING 試驗（NCT03840772）完整發表結果，確認療效數據（ORR、PFS）
- 補齊 DG001：取得 FDA/EMA 核准仿單進行安全性初評（台灣未上市，可參閱國際仿單）
- 補齊 DG002：查詢 DrugBank DB08871 確認完整 MOA 及 DrugBank categories
- 確認 eribulin 全球核准適應症詳細清單，特別是脂肪肉瘤亞型範圍
- 評估台灣藥品取得路徑：恩慈療法（compassionate use）或臨床試驗申請
- **其他 9 個預測適應症**：目前均建議 Hold，待後續研究發表再重新評估；卵巢黏液樣脂肪肉瘤（排名第 5）因與 FDA 已核准的脂肪肉瘤存在類比關係，可標記為 Research Question 持續追蹤
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

