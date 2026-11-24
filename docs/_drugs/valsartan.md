---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 924
evidence_level: L5
indication_count: 6
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
last_modified_at: 2026-11-24
description: "Valsartan：預測新適應症為惡性高血壓腎病變（證據等級 L5）。原適應症：高血壓"
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Valsartan：從高血壓到惡性高血壓腎病變
{: .text-alpha }

## 一句話總結

Valsartan 是血管張力素 II 第一型受體（AT1）阻斷劑，知識圖譜記錄的原適應症為高血壓。
TxGNN 模型預測它可能對**惡性高血壓腎病變 (malignant hypertensive renal disease)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇間接文獻**（內容為另一種藥物 avosentan 的前臨床研究），證據非常有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（知識圖譜記錄；本次整理的香港許可證資料未載明適應症文字） |
| 預測新適應症 | 惡性高血壓腎病變 |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 78 張／共 78 張） |
| 許可證數 | 78 張（有效 78 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Valsartan 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「血管收縮素 II 是由血管收縮素 I 在血管收縮素轉化酶（ACE，激肽酶 II）催化的反應中形成。血管收縮素 II 是腎素-血管收縮素系統的主要升壓物質，其作用包括血管收縮、刺激醛固酮的合成與釋放、心臟刺激，以及腎臟對鈉的再吸收。[…] Diovan（valsartan）藉由選擇性阻斷血管收縮素 II 與許多組織（例如血管平滑肌及腎上腺）中 AT 1 受體的結合，阻斷血管收縮素 II 的血管收縮及醛固酮分泌作用。」英文原文："Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Diovan (valsartan) blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland."（[DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213)，版本日期 2026-08-11；查閱日期 2026-11-19）。根據已知資訊，Valsartan 屬於 AT1 受體阻斷劑（ARB）類別，可阻斷腎素-血管張力素系統對血管收縮的作用，用於高血壓治療。

惡性高血壓腎病變是嚴重高血壓造成的腎臟損傷，和原本的高血壓適應症在病理上相連。在機轉上，阻斷 AT1 受體可降低血壓，並可能減輕腎臟的血管與纖維化損傷，因此模型預測具有生物學上的合理性。

不過，這只是推論。唯一取得的文獻研究的是內皮素拮抗劑 avosentan，並非 valsartan，因此只能視為間接線索。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | 前臨床（不同藥物） | Pharmacological Research | 在過度表現人類腎素與血管張力素原基因的轉基因大鼠中，內皮素拮抗劑 avosentan 在不引起液體滯留的劑量下，對高血壓腎病變有保護作用；此研究未使用 valsartan |

---

## 香港上市資訊

以下為本次整理到的部分許可證（含本藥成分的許可證包括單一成分與複方製劑；張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表）。資料中未載明劑型與核准適應症文字。

<!-- review:begin hk-lic-20261117-valsartan-1 -->

> **查核更正（2026-11-24）**：原文為「以下為本次整理到的許可證（共列出 5 張，總數至少 20 張，清單可能不完整）。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-valsartan-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-62376 | PMS-VALSARTAN TABLETS 320MG | 單一成分 | TRENTON-BOMA LTD | 有效 |
| HK-60971 | VALSACOR FILM-COATED TABLETS 80MG | 單一成分 | TRENTON-BOMA LTD | 有效 |
| HK-49137 | DIOVAN TAB 80MG | 單一成分 | NOVARTIS PHARMACEUTICALS (HK) LIMITED | 有效 |
| HK-49138 | DIOVAN TAB 160MG | 單一成分 | NOVARTIS PHARMACEUTICALS (HK) LIMITED | 有效 |
| HK-66401 | VALSARTAN TEVA TABLETS 80MG | 單一成分 | TEVA PHARMACEUTICAL HONG KONG O/B TEVA PHARMACEUTICAL HONG KONG LIMITE… | 有效 |

上表列出其中 5 張（共 78 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：肝衰竭、肝病、胰臟炎、膽囊疾病、血管性水腫（含遺傳性及腎素-血管張力素系統阻斷劑引起者）、全身性紅斑狼瘡、缺鉀、糖尿病及糖尿病酮酸中毒、高尿酸血症、痛風、嗜中性白血球低下、顆粒球缺乏症、低血壓、副甲狀腺機能亢進、高血鈣、腎鈣質沉著症、磷代謝異常、肝性昏迷與肝性腦病變、新生兒黃疸、無尿、腎動脈阻塞、腎功能不全。
- **藥物交互作用**（資料庫共 100 筆，以下為主要者）：
  - 重大：氯化鉀、碳酸氫鉀（有高血鉀風險）
  - 中度：多種胰島素製劑、Exenatide、Hydrocortisone、Eluxadoline、含電解質之聚乙二醇 3350

仿單警語與禁忌的正式內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高，但沒有臨床試驗，唯一文獻研究的是另一種藥物，直接證據不足，屬 L5。
- 知識圖譜中的禁忌關聯涵蓋腎功能不全、腎動脈阻塞與高血鉀風險，對腎病變族群需審慎評估。

**若要推進需要：**
- 搜尋 valsartan 或其他 ARB 用於惡性高血壓腎病變的臨床與觀察性研究
- 取得原廠仿單的警語與禁忌，以及作用機轉資料
- 設計針對腎功能與血鉀監測的安全計畫
- 釐清香港許可證實際核准的適應症文字

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「以下為本次整理到的許可證（共列出 5 張，總數至少 20 張，清單可能不完整）。」→「以下為本次整理到的部分許可證（含本藥成分的許可證包括單一成分」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

