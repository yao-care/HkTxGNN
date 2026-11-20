---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 7
monitor_inn: "METHOTREXATE"
predicted_indications: ["pulmonary blastoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "Hodgkins lymphoma", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
last_modified_at: 2026-11-20
description: "Methotrexate：預測新適應症為肺母細胞瘤 (Pulmonary Blastoma)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症文字"
---

# Methotrexate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Methotrexate：從急性淋巴性白血病到肺母細胞瘤
{: .text-alpha }

## 一句話總結

Methotrexate（甲氨蝶呤）是抗代謝類藥物，在知識圖譜中記錄的原有用途包括急性淋巴性白血病、類風濕性關節炎、乾癬、蕈狀肉芽腫與非何杰金氏淋巴瘤。
TxGNN 模型排名第一的預測是**肺母細胞瘤 (Pulmonary Blastoma)**（分數 0.9945），但該預測沒有任何臨床試驗或文獻佐證，僅屬模型推論。
本報告把資料較多的候選另列於下，其中**橫紋肌肉瘤**與**何杰金氏淋巴瘤**有較多相關資料，但直接證據仍有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症文字；知識圖譜記錄的相關疾病包括急性淋巴性白血病、類風濕性關節炎、乾癬、非何杰金氏淋巴瘤（僅為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 肺母細胞瘤 (Pulmonary Blastoma)（排名第一） |
| TxGNN 預測分數 | 0.9945 |
| 證據等級 | L5（無臨床試驗與文獻） |
| 香港上市 | 上市中（有效許可證 9 張／共 9 張） |
| 許可證數 | 9 張（有效 9 張） |
| 核准數 | 9 張許可證（皆為單一成分） |
| 建議決策 | Hold |

<!-- review:begin hk-lic-20261117-methotrexate-2 -->

> **查核更正（2026-11-17）**：原文為「8 張許可證（皆為單一成分）」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69160 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-methotrexate-2 -->

## 為什麼這個預測合理？

根據美國 FDA 核准的 Methotrexate 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Methotrexate 抑制二氫葉酸還原酶。二氫葉酸必須先經此酶還原為四氫葉酸，才能在嘌呤核苷酸及胸苷酸的合成中作為一碳基團的載體而被利用。」英文原文："Methotrexate inhibits dihydrofolic acid reductase. Dihydrofolates must be reduced to tetrahydrofolates by this enzyme before they can be utilized as carriers of one-carbon groups in the synthesis of purine nucleotides and thymidylate."（[DailyMed: Jylamvo (methotrexate) prescribing information, SHORLA ONCOLOGY INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96e931f5-51ae-4bdf-a441-bb0dd26d4c0e)，版本日期 2026-11-05；查閱日期 2026-11-19）。Methotrexate 一般被認為是抗葉酸藥物，可抑制二氫葉酸還原酶（DHFR）與胸苷酸合成，影響快速增殖細胞的 DNA 合成。這是一般藥理知識，並非來自本次彙整的 MOA 資料。

肺母細胞瘤是增殖活躍的胚胎型腫瘤，從抗增殖機轉來看有理論上的合理性，但這純屬計算預測。沒有任何試驗或文獻直接研究 methotrexate 用於肺母細胞瘤，因此不能視為有臨床支持。

## 各預測適應症的證據概況

| 預測適應症 | TxGNN 分數 | 直接證據 | 證據等級 | 建議 |
|-----------|-----------|---------|---------|------|
| 肺母細胞瘤 | 0.9945 | 無 | L5 | Hold |
| 原發性肺淋巴瘤 | 0.9945 | 僅間接文獻（病例報告、一般淋巴瘤與中樞神經淋巴瘤研究） | L5 | Hold |
| 高分化胎兒型肺腺癌 | 0.9942 | 無 | L5 | Hold |
| 何杰金氏淋巴瘤 | 0.9932 | 早期 VBM 方案研究（PMID 14635074、21592816） | L3 | Research Question |
| 橫紋肌肉瘤 | 0.9925 | 高劑量 methotrexate 的 Phase 2 研究（PMID 9329466） | L2 | Research Question |
| 腦膜旁胚胎型橫紋肌肉瘤 | 0.9921 | 無 | L5 | Hold |
| 陰道葡萄狀胚胎型橫紋肌肉瘤 | 0.9921 | 無 | L5 | Hold |

註：原發性肺淋巴瘤的文獻主要涉及中樞神經淋巴瘤或一般淋巴瘤，沒有肺部特定的 methotrexate 研究，依規則等級下修為 L5。何杰金氏淋巴瘤與橫紋肌肉瘤的等級以資料中直接研究該疾病的文獻為準，但這些研究年代久遠、規模小且多為非隨機設計，等級應視為上限。

## 臨床試驗證據

排名第一的肺母細胞瘤：目前無相關臨床試驗登記。

為供參考，下表為排名第五的橫紋肌肉瘤候選所列試驗，其中多數並未直接研究橫紋肌肉瘤：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00357084](https://clinicaltrials.gov/study/NCT00357084) | Phase 2 | 完成 | 53 | Methotrexate 合併糖皮質素治療造血幹細胞移植後急性移植物抗宿主病，並非橫紋肌肉瘤研究 |
| [NCT00253552](https://clinicaltrials.gov/study/NCT00253552) | NA | 終止 | 4 | 使用 filgrastim 動員骨髓之移植先導研究，非 methotrexate 研究 |
| [NCT00003273](https://clinicaltrials.gov/study/NCT00003273) | Phase 2 | 撤銷 | 0 | 幼童惡性腦瘤高劑量化療，無實際資料 |
| [NCT00112645](https://clinicaltrials.gov/study/NCT00112645) | Phase 1 | 完成 | 10 | 小兒實體瘤異體移植毒性研究，methotrexate 為輔助成分 |

## 文獻證據

下表為最相關的文獻（橫紋肌肉瘤與何杰金氏淋巴瘤）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9329466](https://pubmed.ncbi.nlm.nih.gov/9329466/) | 1997 | Phase 2 試驗 | J Pediatr Hematol Oncol | 高劑量 methotrexate 用於未經治療的高風險不可切除或轉移性橫紋肌肉瘤兒童與青少年 |
| [14635074](https://pubmed.ncbi.nlm.nih.gov/14635074/) | 2003 | 臨床研究 | Cancer | VBM（vinblastine、bleomycin、methotrexate）加放療用於早期何杰金氏淋巴瘤 |
| [21592816](https://pubmed.ncbi.nlm.nih.gov/21592816/) | 2012 | Review | Crit Rev Oncol Hematol | VBM 方案治療早期何杰金氏淋巴瘤，完全緩解率 94-100%，早期試驗有明顯肺毒性 |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | 先導研究 | Oncotarget | 小兒節律式四藥方案 |
| [12376811](https://pubmed.ncbi.nlm.nih.gov/12376811/) | 2002 | 病例報告/系列 | Pediatr Nephrol | 高流量血液透析移除 methotrexate，用於高劑量輸注後腎毒性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-29818 | METHOTREXAT-EBEWE CONC FOR IV INF 5000MG | 未載明 | 未載明 |
| HK-67078 | METHOTREXATE TABLETS 2.5MG | 未載明 | 未載明 |
| HK-16293 | METHOTREXATE INJ 50MG/2ML | 未載明 | 未載明 |
| HK-36225 | METHOTREXAT TAB 2.5MG (EBEWE) | 未載明 | 未載明 |
| HK-27062 | EMTHEXATE TAB 2.5MG | 未載明 | 未載明 |

共 9 張有效單一成分許可證，上表僅列出 5 張。

<!-- review:begin hk-lic-20261117-methotrexate-1 -->

> **查核更正（2026-11-17）**：原文為「共 8 張有效單一成分許可證」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69160 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-methotrexate-1 -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗代謝／抗葉酸類） |
| 骨髓抑制風險 | 知識圖譜記錄白血球減少、血小板減少、貧血為禁忌相關疾病，提示有骨髓抑制風險 |
| 監測項目 | 全血球計數、肝腎功能；詳細項目請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **知識圖譜記錄的禁忌相關疾病**（非仿單內容）：肝衰竭、肝病、腎病、膽囊疾病、血小板減少、白血球減少、貧血（含巨球性貧血）、消化性潰瘍、潰瘍性結腸炎、發炎性腸病、口腔炎、間質性肺病、肺纖維化、物質濫用／依賴、免疫系統疾病、膿尿輸尿管。
- **藥物交互作用**：共查得 100 筆，主要為 Major 等級者包括 rabeprazole、amoxicillin、acetylsalicylic acid（阿斯匹靈）；另有多項 Moderate 等級，例如 doxycycline、tetracycline、clarithromycin、類固醇（hydrocortisone、dexamethasone 等）、mesalazine、amphotericin B。
- 文獻中亦出現 methotrexate 相關淋巴增生性疾病、肺毒性及高劑量後腎毒性的訊號。

香港仿單的警語與禁忌資料尚未取得，安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的肺母細胞瘤沒有任何臨床試驗或文獻，僅為模型預測（L5）。
- 證據較多的橫紋肌肉瘤與何杰金氏淋巴瘤只有小型、年代久遠的研究，且現行標準治療已有其他方案，尚不足以支持推進。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字。
- 補充 DrugBank 的作用機轉資料。
- 針對肺母細胞瘤與原發性肺淋巴瘤做專題文獻回顧。
- 若選擇橫紋肌肉瘤或何杰金氏淋巴瘤，需評估 methotrexate 相對現行標準方案是否有附加價值，並規劃肝腎功能、血液學與肺毒性監測。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「共 8 張有效單一成分許可證」→「共 9 張有效單一成分許可證」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-17 | 「8 張許可證（皆為單一成分）」→「9 張許可證（皆為單一成分）」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Jylamvo (methotrexate) prescribing information, SHORLA ONCOLOGY INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=96e931f5-51ae-4bdf-a441-bb0dd26d4c0e) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

