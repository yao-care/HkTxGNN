---
layout: default
title: Polymyxin B
parent: 中證據等級 (L3-L4)
nav_order: 711
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-24
description: "Polymyxin B：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L4）。原適應症：許可證資料未載明"
monitor_inn: "POLYMYXIN B"
predicted_indications: ["bronchitis", "laryngotracheitis"]
---

# Polymyxin B
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

## Polymyxin B：從細菌感染（原適應症資料缺漏）到支氣管炎
{: .text-alpha }

## 一句話總結

Polymyxin B 是一種陽離子多肽類抗生素，主要針對革蘭氏陰性菌。本次資料中，香港許可證未提供原適應症文字。
TxGNN 模型預測分數最高的新適應症為**支氣管炎 (Bronchitis)**，目前**無臨床試驗登記**，有 **12 篇文獻**，但多為間接或安全性相關研究。
另外兩個預測適應症中，**結膜炎 (Conjunctivitis)** 的證據最強，有多項 RCT，但多為與 trimethoprim 的複方製劑。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 0.9987 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證 28 張／共 28 張） |
| 許可證數 | 28 張（有效 28 張） |
| 建議決策 | Hold |

其他預測適應症：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|-----------|-----------|---------|---------|
| 2 | 喉氣管炎 (Laryngotracheitis) | 0.9962 | L5 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Polymyxin B 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「Polymyxin B sulfate對除變形桿菌屬（Proteus）以外的幾乎所有革蘭氏陰性桿菌具有殺菌作用。Polymyxins可增加細菌細胞膜的通透性，導致細胞死亡。所有革蘭氏陽性菌、真菌及革蘭氏陰性球菌均對polymyxin B具抗藥性。有關FDA針對本藥品所認可的感受性試驗判讀標準、相關試驗方法及品質管制標準的具體資訊，請參閱：www.fda.gov/STIC。」英文原文："Polymyxin B sulfate has a bactericidal action against almost all gram-negative bacilli except the Proteus group. Polymyxins increase the permeability of bacterial cell membrane leading to death of the cell. All gram positive bacteria, fungi, and gram-negative cocci are resistant to polymyxin B. For specific information regarding susceptibility test criteria and associated test methods and quality control standards recognized by FDA for this drug, please see: www.fda.gov/STIC."（[DailyMed: Polymyxin B (polymyxin b sulfate) prescribing information, Xellia Pharmaceuticals USA LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b56f18c0-ef5e-4ed9-a5af-f79f3cd189b6)，版本日期 2026-06-22；查閱日期 2026-11-19）。根據已知資訊，Polymyxin B 是陽離子多肽類抗生素，可破壞革蘭氏陰性菌的外膜，因此對呼吸道的革蘭氏陰性菌感染（例如多重抗藥性的氣管支氣管炎）在機轉上具合理性。

不過文獻同時顯示，吸入性 Polymyxin B 可作為非特異性支氣管激發劑（促組織胺釋放、引起支氣管收縮），在氣喘和慢性支氣管炎患者身上是重要的安全疑慮。其餘證據多為老舊、小規模或非臨床研究。極高的 TxGNN 分數僅為計算預測，不能取代臨床證據。

結膜炎方面，Polymyxin B 外用（通常與 trimethoprim 合併）可涵蓋多種眼表病原菌，與 moxifloxacin 的比較試驗支持其療效。但證據針對的是固定劑量複方而非單方，且此適應症在臨床上已確立，可能已是既有核准用途，而非真正的藥物再利用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

（結膜炎的 RCT 證據請見下方文獻，其試驗階段需對照全文確認。）

---

## 文獻證據

### 支氣管炎（排名 1）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Review/Meta-analysis | Infection | 比較 Polymyxin B 與其他抗菌藥物治療綠膿桿菌或鮑氏不動桿菌所致呼吸器相關肺炎與氣管支氣管炎（間接證據） |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Case series | Diagn Microbiol Infect Dis | 19 名患者以吸入性 Polymyxin B 治療多重抗藥性革蘭氏陰性菌呼吸道感染，規模小、無對照 |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | 臨床報告 | J Kans Med Soc | 全身性 gentamicin 加 Polymyxin B 噴霧治療綠膿桿菌氣管支氣管炎 |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | 實驗性臨床研究 | Lung | 氣喘與慢性支氣管炎患者吸入 Polymyxin B 後的支氣管反應（安全性訊號） |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | 實驗性臨床研究 | Orvosi Hetilap | Polymyxin B 誘發非特異性支氣管激發（安全性訊號） |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | 安全性通報 | Ann Intern Med | 吸入 Polymyxin B 的危險性 |

### 結膜炎（排名 3，證據最強）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23092529](https://pubmed.ncbi.nlm.nih.gov/23092529/) | 2013 | RCT | J Pediatr | 單盲 RCT，比較 Polymyxin B-trimethoprim 與 moxifloxacin 治療兒童急性結膜炎 |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | 多中心比較 Polymyxin B/trimethoprim 與 moxifloxacin 治療細菌性結膜炎的臨床起效速度 |
| [19043943](https://pubmed.ncbi.nlm.nih.gov/19043943/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Moxifloxacin 對比 Polymyxin B/trimethoprim 用於兒童細菌性結膜炎 |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | 臨床研究 | J Antimicrob Chemother | 230 名患者的隨機雙盲多中心試驗，trimethoprim-polymyxin B 與 neomycin-polymyxin B-gramicidin 及 chloramphenicol 皆有效 |
| [2850891](https://pubmed.ncbi.nlm.nih.gov/2850891/) | 1988 | 雙盲試驗 | Curr Med Res Opin | 42 名患者，與 chloramphenicol 眼膏療效無顯著差異 |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Review | Drugs | 比較 16 種外用眼科抗菌製劑，Polymyxin B 針對革蘭氏陰性菌 |
| [26922212](https://pubmed.ncbi.nlm.nih.gov/26922212/) | 2016 | 個案報告 | Ann Allergy Asthma Immunol | Polymyxin B-trimethoprim 眼藥水引起過敏性休克（安全性訊號） |

### 喉氣管炎（排名 2）

目前無相關文獻。

---

## 香港上市資訊

香港共有 28 張含本藥成分的許可證（全部有效；皆為複方）。資料中未提供劑型與核准適應症文字。以下列出其中 5 張：

<!-- review:begin hk-lic-20261117-polymyxin_b-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 20 張有效許可證，皆為單一成分登記，無取消紀錄。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 28 張含本藥成分的許可證（全部有效；皆為複方）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-polymyxin_b-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-02068 | TERRAMYCIN OPHTHALMIC OINT | 複方 | PFIZER CORPORATION HONG KONG LIMITED | 有效 |
| HK-41904 | OTOZAMBON EAR DROPS | 複方 | ZENFIELDS (H.K.) LIMITED | 有效 |
| HK-53520 | DEXATROL EYE/EAR DROPS | 複方 | MEDEXROM LTD | 有效 |
| HK-30056 | POLYCIN OINT | 複方 | EUROPHARM LAB CO LTD | 有效 |
| HK-52786 | OPSACIN STERILE EYE DROPS | 複方 | ROCO INTERNATIONAL MEDICAL COMPANY LIMITED | 有效 |

上表列出其中 5 張（共 28 張）。

<!-- licenses:end -->

從品名可看出，多數產品為眼用、耳用或外用製劑。

---

## 安全性考量

- **吸入風險**：文獻顯示吸入性 Polymyxin B 可引發支氣管收縮，氣喘及慢性支氣管炎患者尤需注意。
- **過敏反應**：有 Polymyxin B-trimethoprim 眼藥水引起過敏性休克的個案報告。
- **藥物交互作用**：資料庫共記錄 73 項交互作用。主要（Major）等級包括：
  - Amikacin
  - Botulinum toxin type A
  - Cisatracurium
  - Cidofovir
  - Deferasirox
  - 靜脈注射人類免疫球蛋白
  - 顯影劑（Iothalamic acid、Diatrizoate）
  - 活性霍亂疫苗

  中度（Moderate）等級包括 Capreomycin、Mesalazine、Ethinylestradiol、Estradiol 等。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（支氣管炎）；結膜炎可 Proceed with Guardrails**

**理由：**
- 支氣管炎的預測僅有間接、老舊或小規模的證據，且吸入性 Polymyxin B 有支氣管收縮的安全疑慮，目前不宜推進。喉氣管炎僅有模型預測，且該病多為病毒性，機轉不吻合。
- 結膜炎有多項與 moxifloxacin 或 chloramphenicol 的隨機比較研究，但證據針對 Polymyxin B/trimethoprim 複方，且此用途在臨床上已確立，可能屬既有適應症而非新用途。

**若要推進需要：**
- 補充香港許可證的原適應症、劑型與核准適應症資料，以及仿單的警語與禁忌症
- 取得詳細的作用機轉資料
- 對照文獻全文，確認結膜炎研究的試驗階段與設計
- 結膜炎應限於細菌性（非病毒性或過敏性），並考量抗菌藥物管理與當地抗藥性
- 支氣管炎若要繼續評估，需先釐清給藥途徑（吸入）的安全性，並設計針對性的臨床研究

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 20 張有效許可證，皆為單一成分登記，無取消紀錄。」→「香港共有 28 張含本藥成分的許可證（全部有效；皆為複方）。」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Polymyxin B (polymyxin b sulfate) prescribing information, Xellia Pharmaceuticals USA LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b56f18c0-ef5e-4ed9-a5af-f79f3cd189b6) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

