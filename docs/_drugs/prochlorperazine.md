---
layout: default
title: Prochlorperazine
parent: 僅模型預測 (L5)
nav_order: 736
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "Prochlorperazine"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy", "manic bipolar affective disorder"]
description: "Prochlorperazine：預測新適應症為視網膜失養症 (retinal dystrophy with or without extraocular anomalies)（證據等級 L5）。香港藥劑製品註冊：13 張（有效 13 張）"
---

# Prochlorperazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Prochlorperazine: 視網膜失養症 (retinal dystrophy with or without extraocular anomalies)
{: .text-alpha }

## 一句話總結

Prochlorperazine 是吩噻嗪（phenothiazine）類藥物，原本用於思覺失調症。
TxGNN 模型預測分數最高的新適應症是**視網膜失養症 (retinal dystrophy with or without extraocular anomalies)**，但目前**沒有任何臨床試驗或文獻**支持。
相對之下，排名第 10 的**躁期雙相情緒障礙 (manic bipolar affective disorder)** 在機轉上較合理，有 **7 篇間接文獻**，但沒有臨床試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 視網膜失養症 (retinal dystrophy with or without extraocular anomalies) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 13 張／共 13 張） |
| 許可證數 | 13 張（有效 13 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

ChEMBL（EMBL-EBI）收錄的 Prochlorperazine 作用機轉（非官方翻譯）：「多巴胺 D2 受體拮抗劑」英文原文："Dopamine D2 receptor antagonist"（[ChEMBL CHEMBL728 (prochlorperazine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL728)，CC BY-SA 3.0；查閱日期 2026-11-19）。Prochlorperazine 屬於吩噻嗪類藥物，一般認為其作用為多巴胺 D2 受體拮抗，這也是抗精神病藥效的基礎。

首位預測的視網膜失養症，是由光受體或視網膜色素上皮功能的單基因缺陷所致，D2 拮抗作用與這些路徑之間沒有已知關聯。此高分應視為模型預測，並無試驗或文獻佐證，**無法認為機轉上合理**。

本次預測清單中的其他前幾名（水腦無腦畸形、先天性糖基化異常、X 連鎖近視、CMT1G、多小腦回畸形、非典型甘胺酸腦病變等）同樣缺乏機轉連結，也沒有任何證據。唯一例外是排名第 10 的躁期雙相情緒障礙：D2 拮抗正是抗精神病藥用於急性躁狂與躁動的機轉，與原適應症一致。不過現有文獻多為 1959–1965 年的病例報告與調查，證據屬間接性質，且已有研究更充分的抗精神病藥可用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。（首位預測及排名第 10 的躁期雙相情緒障礙均無登記試驗。）

---

## 文獻證據

首位預測（視網膜失養症）目前無相關文獻。以下為排名第 10 的躁期雙相情緒障礙之文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19461391](https://pubmed.ncbi.nlm.nih.gov/19461391/) | 2009 | Review | Journal of Psychiatric Practice | 回顧懷孕期間使用抗精神病藥的使用情形與安全性 |
| [26819726](https://pubmed.ncbi.nlm.nih.gov/26819726/) | 2015 | Cohort | Journal of Pharmaceutical Health Care and Sciences | 以 FAERS 通報資料評估抗精神病藥與高血糖不良事件的關聯 |
| [14242542](https://pubmed.ncbi.nlm.nih.gov/14242542/) | 1965 | Review | Obstetrics and Gynecology | 產褥期嚴重精神疾患的臨床處置建議 |
| [14233737](https://pubmed.ncbi.nlm.nih.gov/14233737/) | 1964 | Review | American Journal of Psychiatry | 電痙攣治療併用吩噻嗪類與利血平的調查報告 |
| [14222730](https://pubmed.ncbi.nlm.nih.gov/14222730/) | 1964 | Review | L'Encephale | 精神抑制劑治療過程中出現的精神失調表現 |
| [14062306](https://pubmed.ncbi.nlm.nih.gov/14062306/) | 1963 | Review | La Tunisie Medicale | 躁動的本質與一般醫師的急診處置 |
| [13617778](https://pubmed.ncbi.nlm.nih.gov/13617778/) | 1959 | Case report | Annales Medico-Psychologiques | 輕度躁鬱症患者使用 prochlorperazine 後出現意識混亂、夢樣發作 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46144 | SERATIL TAB 5MG (WHITE) | 未載明 | 未載明 |
| HK-06335 | METIL TAB 5MG | 未載明 | 未載明 |
| HK-61940 | PROCHLOR TABLETS 5MG | 未載明 | 未載明 |
| HK-11609 | PERATIL TAB 5MG (BLUE) | 未載明 | 未載明 |
| HK-50611 | METIL-B TAB 5MG | 未載明 | 未載明 |

香港共有 13 張含本藥成分的許可證（全部有效；皆為單一成分），上表僅列出其中 5 張。

<!-- review:begin hk-lic-20261117-prochlorperazine-1 -->

> **查核更正（2026-11-17）**：原文為「本品共有 12 張有效單方許可證，上表僅列出其中 5 張。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 13 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-prochlorperazine-1 -->

---

## 安全性考量

- **知識圖譜中的禁忌疾病**（非仿單文字）：涵蓋心血管（高血壓、直立性低血壓、長 QT 症候群、尖端扭轉型心室頻脈、冠狀動脈疾病、心肌梗塞）、神經（癲癇、基底核疾病、局部手部肌張力不全、眼瞼痙攣、多系統萎縮）、血液（血小板低下、嗜中性白血球低下、顆粒球缺乏症）、肝腎與消化（肝病、腎病、膽囊疾病、胃潰瘍）、代謝（高血糖、肥胖）、其他（良性攝護腺增生、物質濫用/依賴、女性乳癌）等。
- **藥物交互作用**：資料庫共 100 筆，其中列為**重大 (Major)** 的有 **Bupropion** 與 **Potassium citrate**；其餘多為中度，如降血糖藥（Metformin、Pioglitazone、Alogliptin、Acarbose、Canagliflozin、Chlorpropamide、Albiglutide）、抗膽鹼藥（Atropine、Hyoscyamine、Glycopyrronium）、Morphine、Clarithromycin、Epinephrine 等。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測的視網膜失養症及其他前九名預測，皆無臨床試驗、無文獻，也找不到任何機轉連結，僅為模型運算的結果，不足以支持推進。
- 排名第 10 的躁期雙相情緒障礙在機轉上較合理（證據等級 L4，可列為研究問題），但文獻老舊且屬間接證據，已有證據充分的替代藥物。

**若要推進需要：**
- 取得完整作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症，以進行安全性篩選
- 若欲探索躁狂適應症：進行系統性文獻回顧，並與現有抗精神病藥比較是否有明確優勢
- 對於視網膜失養症等罕見遺傳疾病：需先有前臨床或機轉研究，才值得重新評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本品共有 12 張有效單方許可證，上表僅列出其中 5 張。」→「香港共有 13 張含本藥成分的許可證（全部有效；皆為單一成分」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [ChEMBL CHEMBL728 (prochlorperazine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL728) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

