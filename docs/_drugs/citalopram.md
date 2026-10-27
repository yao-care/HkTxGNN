---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Citalopram：預測新適應症為強迫症 (Obsessive-Compulsive Disorder)（證據等級 L5）。原適應症：焦慮症、神經症、輕鬱症、單極性憂鬱症、內因性憂鬱症、重度憂鬱症"
monitor_inn: "CITALOPRAM"
predicted_indications: ["obsessive-compulsive disorder", "schizotypal personality disorder", "paranoid personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)"]
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Citalopram：從憂鬱症與焦慮症到強迫症
{: .text-alpha }

## 一句話總結

Citalopram 是一種選擇性血清素再攝取抑制劑（SSRI），原本用於憂鬱症與焦慮症等情緒障礙的治療。
TxGNN 模型預測它可能對**強迫症 (Obsessive-Compulsive Disorder, OCD)** 有效，
目前有 **4 個臨床試驗**和 **15 篇文獻**支持這個方向，但試驗多屬 SSRI 類別層級的證據，並非 citalopram 專屬的 Phase 3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 焦慮症、神經症、輕鬱症、單極性憂鬱症、內因性憂鬱症、重度憂鬱症（香港許可證未載明核准適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 強迫症 (Obsessive-Compulsive Disorder) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L1（僅依類別層級證據，屬保守上限，需先確認 citalopram 試驗組別） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Citalopram 屬於 SSRI，透過抑制血清素再攝取，提高突觸間隙的血清素濃度。目前缺乏詳細的作用機轉資料，上述為 SSRI 類別的已知機轉。

血清素系統失調被認為與強迫症的病理有密切關係，SSRI 也是強迫症的一線藥物治療。文獻如〈Obsessive compulsive disorder: serotonin and beyond〉也闡述了這一點。憂鬱症、焦慮症與強迫症常共病，且共享血清素相關的神經機轉，因此機轉上可能適用於強迫症。

Citalopram 本身在強迫症的直接資料包括成人、難治型及兒童青少年的開放標籤研究與初步研究。不過，這些研究規模小、多為開放標籤。所納入的臨床試驗多屬 SSRI 類別層級或以其他藥物為對照，**沒有一項已確認為 citalopram 專屬的 Phase 3 RCT**，因此 L1 等級應視為保守上限。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | 完成 | 124 | 兒童強迫症對 SRI 部分反應者，評估認知行為治療是否提升 SRI 療效（需確認 citalopram 角色） |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | 完成 | 78 | 曝露與反應預防（ERP）、SSRI 及兩者合併用於強迫症，並探討療效預測因子（未確認 citalopram 為特定組別） |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | 完成 | 158 | 團體認知行為治療 vs. fluoxetine 用於強迫症（所用藥物為 fluoxetine，非 citalopram） |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | NA | 完成 | 43 | 強迫症患者腸道菌相的先導研究，非介入性，與 citalopram 療效無直接關聯 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | 系統性回顧 | Expert Opin Pharmacother | 強迫型人格障礙（OCPD）藥物治療的 RCT 系統性回顧，與 OCD 不同 |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | 臨床研究 | Eur Psychiatry | 難治型強迫症：citalopram 單用 vs. 併用 clomipramine（16 人，隨機開放標籤） |
| [15089116](https://pubmed.ncbi.nlm.nih.gov/15089116/) | 2004 | 世代／藥動學 | CNS Drugs | 初步探討強迫症患者 citalopram 血中濃度與臨床反應的關係 |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | 開放標籤研究 | Psychiatry Clin Neurosci | 15 名兒童青少年強迫症，8 週 citalopram 治療的初步報告 |
| [9466233](https://pubmed.ncbi.nlm.nih.gov/9466233/) | 1997 | 開放標籤試驗 | J Child Adolesc Psychopharmacol | 23 名兒童青少年，10 週後 Y-BOCS 由 30 降至 21（p<0.001） |
| [9241005](https://pubmed.ncbi.nlm.nih.gov/9241005/) | 1997 | 單盲研究 | J Clin Psychopharmacol | 比較 fluvoxamine、paroxetine 與 citalopram 在強迫症的抗強迫療效 |
| [9395151](https://pubmed.ncbi.nlm.nih.gov/9395151/) | 1997 | 開放標籤先導研究 | Acta Psychiatr Scand | citalopram 治療強迫症的 24 週開放標籤先導研究 |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | 回顧／評論 | Int Clin Psychopharmacol | 回顧 citalopram 在強迫症的應用 |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | 回顧 | World J Biol Psychiatry | 強迫症的血清素機轉及其他神經傳導路徑 |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | 回顧 | BMJ Clin Evid | 強迫症的流行病學與治療證據回顧 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35361 | CIPRAM TAB 20MG（Lundbeck HK） | 錠劑 | 資料未載明 |
| HK-52953 | EUROPRAM TAB 20MG | 錠劑 | 資料未載明 |
| HK-53084 | APO-CITALOPRAM TAB 20MG | 錠劑 | 資料未載明 |
| HK-53122 | PMS-CITALOPRAM TAB 20MG | 錠劑 | 資料未載明 |
| HK-60203 | AUROPRAM 10 TAB 10MG | 錠劑 | 資料未載明 |

另有 5 張許可證（LOPRAXER 20/40MG、AUROPRAM 20/40、SELON 20MG），合計 10 張，皆為有效的單一成分許可證。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）**：長 QT 症候群（含家族性）、尖端扭轉型心室頻脈、癲癇、雙相情緒障礙、重度情感性疾患、肝病、膽囊疾病、低血鉀、凝血疾病、心臟病與心血管疾病、抗精神病藥惡性症候群、抗利尿激素不當分泌症候群（含腎因性）、血清素症候群。
- **藥物交互作用**：共查得 100 筆，以下為部分代表：
  - 高嚴重度（Major）：Bupropion、Omeprazole、Cimetidine、Lorcaserin、Cisapride、Clarithromycin、Dexfenfluramine、Diethylpropion、Dolasetron
  - 中度（Moderate）：Famotidine、Loperamide、Morphine、Acetylsalicylic acid（阿斯匹靈）、Bisacodyl 等
  - 輕度（Minor）：Aprepitant、Clotrimazole

其中 QT 延長相關藥物（如 cisapride、dolasetron、clarithromycin）及血清素類藥物的併用，需特別留意。

其餘警語與禁忌的仿單資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- SSRI 為強迫症一線用藥，機轉合理，且有多項 citalopram 在成人與兒童強迫症的開放標籤與初步研究支持。
- 但現有臨床試驗多為類別層級或以其他藥物為對照，L1 等級僅屬保守上限，因此需加上防護措施再推進。

**若要推進需要：**
- 確認 NCT00074815、NCT02022709 的 citalopram 組別設計，核實證據等級
- 取得 citalopram 專屬的隨機對照試驗證據（強迫症）
- 取得香港仿單資料（核准適應症、警語與禁忌）
- 評估 QT 延長、血清素症候群與併用藥物交互作用的監測計畫
- 補充詳細作用機轉資料

---

### 其他預測適應症（附註）

TxGNN 另預測 schizotypal、paranoid、schizoid 與 histrionic 人格障礙（分數皆約 99.68%），但目前僅有模型預測，缺乏直接臨床試驗或文獻證據（證據等級 L5），建議決策為 **Hold**。這四者分數相同，可能反映圖譜的共同訊號，而非個別疾病的證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

