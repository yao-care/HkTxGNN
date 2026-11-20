---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
description: "Metronidazole：預測新適應症為肺囊蟲症 (pneumocystosis)（證據等級 L5）。香港藥劑製品註冊：36 張（有效 36 張）"
---

# Metronidazole
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

## Metronidazole: 肺囊蟲症 (pneumocystosis)
{: .text-alpha }

## 一句話總結

Metronidazole 是硝基咪唑類抗菌與抗原蟲藥物，原本用於厭氧菌感染、陰道炎、賈第鞭毛蟲症等。
TxGNN 模型預測它可能對**肺囊蟲症 (Pneumocystosis)** 有效，但目前**沒有臨床試驗**，僅有 **10 篇文獻**，且多為一般性綜述或病例報告，並未直接檢驗 metronidazole 對此疾病的療效，實質證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肺囊蟲症 (pneumocystosis) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 36 張／共 36 張） |
| 許可證數 | 36 張（有效 36 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Metronidazole 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Metronidazole為一種nitroimidazole，在厭氧環境下對大多數絕對厭氧菌發揮抗菌作用。Metronidazole經被動擴散進入菌體，並於敏感厭氧菌的細胞質中被活化後，即被還原；此過程涉及細胞內電子傳遞供體（如ferredoxin），並將一個電子轉移至metronidazole的硝基，從而形成短暫存在的亞硝基自由基。」英文原文："Metronidazole, a nitroimidazole, exerts antibacterial effects in an anaerobic environment against most obligate anaerobes. Once metronidazole enters the organism by passive diffusion and activated in the cytoplasm of susceptible anaerobic bacteria, it is reduced; this process includes intra-cellular electron transport donors such as ferredoxin and transfer of an electron to the nitro group of the metronidazole leading to formation of a short-lived nitroso free radical."（[DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255)，版本日期 2026-11-02；查閱日期 2026-11-19）。Metronidazole 對厭氧菌與部分原蟲有活性，這類活性仰賴硝基咪唑可被還原活化的代謝途徑。

然而，肺囊蟲（*Pneumocystis*）屬於真菌，並不具備對硝基咪唑敏感的代謝途徑。因此 TxGNN 模型（深度學習）給出的高分（0.9999）可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

所檢索到的文獻多為抗寄生蟲藥物綜述與 HIV 伺機性感染報告，只是在其他情境提到 metronidazole（例如病患因腹瀉或阿米巴感染而使用）。肺囊蟲肺炎的標準治療是 trimethoprim-sulfamethoxazole，而非 metronidazole。整體而言，這個預測的合理性低，應視為模型產生的假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | 抗寄生蟲藥物治療總覽，並非針對 metronidazole 治療肺囊蟲症 |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | metronidazole 用於阿米巴與滴蟲症；肺囊蟲肺炎的首選為 TMP-SMX |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | 抗原蟲治療的藥動學依據與美國治療建議 |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | AIDS 感染併發症的治療回顧，肺囊蟲肺炎為最常見 |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV 相關伺機性感染的現況 |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | 抗微生物預防性用藥試驗的評析 |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | 曾因腹瀉接受 metronidazole 與四環素的成人，後來發生肺囊蟲與 CMV 肺炎 |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | 兩例 AIDS 病患；一例以 metronidazole 治療阿米巴痢疾，後續出現肺囊蟲肺炎 |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | AIDS 病患合併 CMV 與阿米巴結腸炎併腸穿孔、腹膜炎 |

---

## 香港上市資訊

以下列出 5 張主要許可證（共 36 張含本藥成分的許可證，全部有效，皆為單一成分）：

<!-- review:begin hk-lic-20261117-metronidazole-1 -->

> **查核更正（2026-11-17）**：原文為「以下列出 5 張主要許可證（共 20 張，皆為有效的單一成分製劑）：」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 36 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-metronidazole-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36789 | METRONIDAZOLE CAP 200MG（Vickmans） | 膠囊 | 資料未載明 |
| HK-52934 | PHARMANIAGA METRONIDAZOLE TAB 200MG | 錠劑 | 資料未載明 |
| HK-66809 | METROMILL SOLUTION FOR INFUSION 500MG/100ML | 輸注液 | 資料未載明 |
| HK-40240 | METRONIDAZOLE IV INFUSION 0.5%（Baxter） | 靜脈輸注液 | 資料未載明 |
| HK-34300 | ROZEX GEL 0.75%（Galderma） | 凝膠 | 資料未載明 |

其他許可證涵蓋口服錠劑與膠囊、靜脈輸注、陰道栓劑（FROTIN SUPP VAGINAL 250MG）及外用凝膠（ROSAMED GEL 0.75%）等劑型。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容，僅供參考）：肝衰竭、肝病、腎臟疾病、癲癇、血液疾病、嗜中性球低下、顆粒球缺乏症、白血球低下、凝血疾病、週邊神經病變、腦部疾病、視神經疾病、充血性心衰竭、糖尿病（含酮酸中毒）、痛風、膽囊疾病、藥物濫用/依賴、皮膚炎等。
- **藥物交互作用**：共查得 100 筆，主要包括：
  - **重大 (Major)**：乙醇（酒精）
  - **中度 (Moderate)**：Paclitaxel、Adalimumab、Trastuzumab emtansine、Ethinylestradiol、Estradiol、Amiodarone、Celecoxib、Butalbital、Amobarbital、Loperamide 等

仿單層級的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅有模型分數支持，無臨床試驗，文獻也沒有直接檢驗 metronidazole 對肺囊蟲症的療效。
- 肺囊蟲屬真菌，機轉上缺乏合理依據，標準治療已明確（TMP-SMX）。

**若要推進需要：**
- 取得 metronidazole 的作用機轉資料，並評估其對 *Pneumocystis* 是否有任何體外活性。
- 取得香港仿單的警語與禁忌資料。
- 若要探索此方向，需先有體外或動物模型的前臨床證據，再考慮臨床研究。

**補充觀察（其他預測適應症）：** 同一份預測清單中，**外陰潰瘍（ulceration of vulva）**（證據等級 L3，有 22 例外陰克隆氏症臨床研究、系統性回顧及阿米巴性潰瘍病例報告）與**帽狀息肉病（cap polyposis）**（L4，有緩解的病例報告）的證據相對較具生物學合理性，可列為後續優先探討的研究問題。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「以下列出 5 張主要許可證（共 20 張，皆為有效的單一成分製劑）：」→「以下列出 5 張主要許可證（共 36 張含本藥成分的許可證，」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: metronidazole prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49360d6f-c8b3-420e-af75-154cf7b05255) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

