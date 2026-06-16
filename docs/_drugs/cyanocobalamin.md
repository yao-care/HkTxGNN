---
layout: default
title: Cyanocobalamin
parent: 中證據等級 (L3-L4)
nav_order: 197
evidence_level: L4
indication_count: 1
---

# Cyanocobalamin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Cyanocobalamin：從維生素B12缺乏症到生物素代謝疾病

## 一句話總結

Cyanocobalamin（氰鈷胺素）是維生素B12的合成形式，長期用於治療維生素B12缺乏症、巨紅血球性貧血及相關神經病變。TxGNN 模型預測它可能對**生物素代謝疾病 (Biotin Metabolic Disease)** 有效，目前有 **15 個臨床試驗**和 **20 篇文獻**與此方向相關，但多數為間接背景研究，直接治療證據仍不足。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素B12缺乏症（巨紅血球性貧血、神經病變） |
| 預測新適應症 | 生物素代謝疾病 (Biotin Metabolic Disease) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Cyanocobalamin 作為維生素B12的合成形式，在體內轉換為活性輔酶後，參與兩條關鍵代謝途徑：甲基丙二酸輔酶A變位酶（methylmalonyl-CoA mutase）反應及甲硫氨酸合成酶（methionine synthase）反應。生物素（biotin）則是另一族B族維生素，作為丙酮酸羧化酶、乙醯輔酶A羧化酶等多種羧化酶的輔因子。兩者在細胞代謝網路中具有高度連通性。

在疾病層面，甲基丙二酸血症（MMA）與生物素酶缺乏症（biotinidase deficiency）同屬有機酸代謝疾病，臨床表現有時相互重疊，且部分患者呈現多種維生素協同反應（megavitamin-responsive），這為TxGNN在知識圖譜中連結兩者提供了節點路徑依據。

然而，**生物素代謝疾病（包括生物素酶缺乏症、全羧化酶合成酶缺乏症）的標準治療是補充生物素本身**，目前無直接機轉證據支持 Cyanocobalamin 可替代或輔助治療此類疾病。TxGNN 高分（0.996）很可能源於知識圖譜中B族維生素代謝節點的高連通性，屬 AI 預測偽陽性風險較高的情境。

---

## 臨床試驗證據

> 注意：以下試驗均未直接研究 Cyanocobalamin 治療生物素代謝疾病，多為B族維生素廣泛補充研究或代謝疾病相鄰領域試驗。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05832190](https://clinicaltrials.gov/study/NCT05832190) | N/A | 終止 | 5 | 減重手術前補充膳食纖維+生物素（biotin）以改善腸道微生物組；唯一直接包含biotin成分的試驗，但已提前終止且樣本極小 |
| [NCT02426775](https://clinicaltrials.gov/study/NCT02426775) | Phase 3 | 完成 | 33 | Carglumic acid（Carbaglu®）用於丙酸血症（PA）或甲基丙二酸血症（MMA）的長期療效評估；MMA為B12反應型有機酸代謝疾病 |
| [NCT00572741](https://clinicaltrials.gov/study/NCT00572741) | N/A | 完成 | 39 | 針對自閉症兒童的氧化壓力與甲基化障礙進行多種B族維生素（含B12）營養干預 |
| [NCT04312152](https://clinicaltrials.gov/study/NCT04312152) | N/A | 不明 | 200 | 雙盲交叉RCT評估CoQ10+維生素B+E複方代謝支持治療對自閉症患者的效果 |
| [NCT01643187](https://clinicaltrials.gov/study/NCT01643187) | Phase 2 | 不明 | 1,000 | 強化食物對營養不良兒童微量營養素狀態（含血清維生素B12）之影響評估 |
| [NCT01173315](https://clinicaltrials.gov/study/NCT01173315) | Phase 2 | 完成 | 75 | 維生素礦物質複方補充對第2型糖尿病神經病變/腎病的影響；含B12成分，針對代謝性合併症 |
| [NCT05687474](https://clinicaltrials.gov/study/NCT05687474) | N/A | 完成 | 6,824 | 比利時新生兒基因體篩查計畫（Baby Detect），篩查包含生物素相關代謝疾病在內的126種遺傳疾病；屬診斷篩查而非治療試驗 |
| [NCT03655223](https://clinicaltrials.gov/study/NCT03655223) | N/A | 招募中（邀請制） | 30,000 | 美國Early Check新生兒前症狀期篩查平台，識別含代謝疾病在內的罕見疾病；屬篩查基礎設施研究 |
| [NCT03444155](https://clinicaltrials.gov/study/NCT03444155) | N/A | 完成 | 30 | 交叉設計評估天然vs.合成維生素B複方的生物利用度差異（含B12） |
| [NCT01558193](https://clinicaltrials.gov/study/NCT01558193) | N/A | 完成 | 202 | 多維生素/礦物質補充（含或不含脂肪酸）對衝動性與攻擊行為的影響；廣義維生素干預研究 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | **與本題最相關**：系統回顧cobalamin、folate、biotin、維生素B1和E的維生素反應性疾病；詳述cobalamin與biotin代謝障礙的鑑別診斷 |
| [958746](https://pubmed.ncbi.nlm.nih.gov/958746/) | 1976 | Review/Case Series | Pediatric Clinics of North America | 維生素反應性胺基酸病（megavitamin-responsive aminoacidopathies）；討論高劑量B族維生素（含B12）對酶活性的輔因子治療效果 |
| [11031989](https://pubmed.ncbi.nlm.nih.gov/11031989/) | 2000 | Review | Ryoikibetsu Shokogun Shirizu | 維生素依賴性症候群綜述；涵蓋B12依賴型代謝疾病的治療原則 |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Molecular Sciences | B12缺乏與神經系統：闡明B12作為succinyl-CoA合成（由methylmalonyl-CoA）及生物素相關途徑的輔酶角色，機轉分析最新 |
| [1909779](https://pubmed.ncbi.nlm.nih.gov/1909779/) | 1991 | Experimental | Pediatric Research | 以¹³C丙酸鹽追蹤丙酸代謝：含4例B12反應型MMA患者，直接顯示cyanocobalamin在有機酸代謝疾病中的輔酶治療效果 |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | 維生素在代謝疾病中的作用機轉：分類維生素依賴性症候群，包含cobalamin依賴型疾病的藥理劑量治療概念 |
| [6152513](https://pubmed.ncbi.nlm.nih.gov/6152513/) | 1983 | Review | Advances in Clinical Chemistry | 維生素反應性先天性代謝錯誤：系統化整理各種維生素（含B12）在先天性代謝疾病中的治療地位 |
| [7004517](https://pubmed.ncbi.nlm.nih.gov/7004517/) | 1980 | Review | Birth Defects Original Article Series | 特定高劑量維生素療法對酶活性的調控：B12等輔因子用於先天性酶缺陷的治療策略 |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine Metabolic Immune Disorders Drug Targets | 維生素與第2型糖尿病：B族維生素（含thiamin、pyridoxine、biotin）在葡萄糖代謝失調中的角色 |
| [36476407](https://pubmed.ncbi.nlm.nih.gov/36476407/) | 2023 | Experimental (Animal) | Journal of Endocrinology | B12缺乏誘發葡萄糖耐受不良與酮症：大鼠模型顯示B12缺乏影響代謝穩態，間接支持B12在代謝疾病中的作用 |

---

## 香港上市資訊

目前 Cyanocobalamin 在香港**無任何藥品許可證登記**（未上市）。如需取得相關藥品，需透過特殊進口或醫院配方管道。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
生物素代謝疾病（生物素酶缺乏症、全羧化酶合成酶缺乏症）的確定治療是補充生物素本身，目前無臨床試驗或高品質文獻直接支持 Cyanocobalamin 作為此類疾病的治療選項。TxGNN 的高預測分數（99.60%）很可能反映知識圖譜中B族維生素代謝節點的高連通性所產生的偽陽性，而非真實的治療潛力。現有15個臨床試驗均與標的適應症無直接關聯（多數為廣泛維生素補充研究），文獻僅支持到機轉層級（L4），尚無臨床療效數據。

**若要推進需要：**
- 取得 Cyanocobalamin 完整作用機轉（MOA）與 DrugBank 分類資料，釐清其與 biotin 代謝途徑的確切交集
- 查閱罕見代謝疾病專家文獻，確認是否有個案報告顯示 B12 補充對生物素代謝疾病有輔助效益
- 優先評估其他 TxGNN 排名較高且具更強直接臨床證據的候選適應症
- 若確需推進，建議先進行回顧性病例系列研究（n ≥ 10），再考慮前瞻性試驗設計
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

