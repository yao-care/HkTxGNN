---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "PANTOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
description: "Pantoprazole：預測新適應症為Duodenal obstruction（證據等級 L5）。香港藥劑製品註冊：49 張（有效 49 張）"
---

# Pantoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Pantoprazole: Duodenal obstruction
{: .text-alpha }

## 一句話總結

Pantoprazole 是質子幫浦抑制劑（PPI），原本用於消化性潰瘍、胃食道逆流、食道炎及 Zollinger-Ellison 症候群等胃酸相關疾病。
需要說明的是，此預測屬於既有適應症的範圍，實際上不是真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Duodenal obstruction |
| TxGNN 預測分數 | 0.9921 |
| 證據等級 | L5（依資料編譯結果；僅 1 個已完成的 Phase 3 試驗，嚴格依本報告判定規則應為 L2，詳見下方說明） |
| 香港上市 | 上市中（有效許可證 49 張／共 49 張） |
| 許可證數 | 49 張（有效 49 張） |
| 建議決策 | Proceed with Guardrails |

> 證據等級說明：依判定規則，L1 需要 ≥2 個已完成的 Phase 3 RCT。目前僅有 1 個已完成的 Phase 3 試驗（NCT02084420），且 Pantoprazole 在該試驗中可能是對照組。文獻中另有數項相關的隨機對照試驗，但多屬間接證據。因此保守來看，證據強度介於 L1 與 L2 之間。

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Pantoprazole 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Pantoprazole 是一種 PPI，透過與胃壁細胞分泌表面的（H +, K + ）-ATPase 酶系統共價結合，抑制胃酸生成的最後步驟。此作用導致基礎及受刺激的胃酸分泌均受到抑制，不論刺激為何。」英文原文："Pantoprazole is a PPI that suppresses the final step in gastric acid production by covalently binding to the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. This effect leads to inhibition of both basal and stimulated gastric acid secretion irrespective of the stimulus."（[DailyMed: Protonix I.V. (pantoprazole sodium) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cde88e6-28f2-4cbe-8c3f-770b05cc0e1b)，版本日期 2026-11-06；查閱日期 2026-11-19）。不過依據已知藥理，Pantoprazole 會不可逆地抑制胃壁細胞上的 H+/K+ ATPase（質子幫浦），這是胃酸分泌的最後一步，因此能降低胃酸、讓潰瘍癒合。

這個預測反映的是模型正確辨認出藥物既有的用途，而非發現新用途。

其他排名較低的預測（潰瘍穿孔、胃空腸潰瘍、十二指腸胃逆流、十二指腸阻塞）的證據強度逐步遞減，詳見結論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | 完成 | 323 | 多中心、隨機、雙盲、活性對照試驗，比較 Ilaprazole 與 Pantoprazole 三合療法（7 天）對胃／十二指腸潰瘍合併幽門螺旋桿菌感染患者的根除效果；Pantoprazole 為試驗藥或對照藥需進一步確認 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 LA 分級 C/D 食道炎的療效與安全性 |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut Liver | Tegoprazan 治療內視鏡切除後人工潰瘍（非 Pantoprazole 專屬） |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | 比較研究 | Am J Gastroenterol | 巴西多中心研究，比較 Pantoprazole 與 Ranitidine 治療十二指腸潰瘍 |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | 比較研究 | Hepato-gastroenterology | 比較 Lansoprazole 與 Pantoprazole 治療活動性十二指腸潰瘍及根除幽門螺旋桿菌 |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole 作用持續時間長，且尚未發現明確藥物交互作用 |
| [21534455](https://pubmed.ncbi.nlm.nih.gov/21534455/) | 2011 | Review | Med Arh | PPI 用於胃食道逆流的治療 |
| [10450061](https://pubmed.ncbi.nlm.nih.gov/10450061/) | 1999 | Review | Pharmacology | 各 PPI 在同毫克劑量下劑量反應與效力相近 |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Review | Int J Clin Pharmacol Ther | CYP2C19 多型性對 PPI 作用的影響 |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | 動物實驗 | Inflammopharmacology | Pantoprazole 併用間質幹細胞對大鼠胃潰瘍的癒合作用 |
| [26439477](https://pubmed.ncbi.nlm.nih.gov/26439477/) | 2016 | 動物實驗 | J Nat Med | 藏紅花素對大鼠吲哚美辛誘發胃損傷的保護作用（Pantoprazole 為對照） |

---

## 香港上市資訊

香港含本藥成分的許可證皆為單一成分，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。以下列出 5 張主要許可證（資料中未收錄劑型與核准適應症文字）：

<!-- review:begin hk-lic-20261117-pantoprazole-1 -->

> **查核更正（2026-11-24）**：原文為「香港共有 20 張有效許可證，皆為單方製劑，目前無已註銷者。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證皆為單一成分，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-pantoprazole-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-44676 | PANTOLOC I.V. INJ 40MG | 單一成分 | TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED | 有效 |
| HK-45019 | PANTOLOC GASTRO-RESISTANT TAB 20MG | 單一成分 | TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED | 有效 |
| HK-63999 | TECTA GASTRO-RESISTANT TABLETS 40MG | 單一成分 | TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED | 有效 |
| HK-59424 | PANTOPRAZOLE SANDOZ TAB 20MG | 單一成分 | SANDOZ HONG KONG LIMITED | 有效 |
| HK-64263 | PANRAZOL ENTERIC COATED TABLETS 20MG | 單一成分 | TEVA PHARMACEUTICAL HONG KONG O/B TEVA PHARMACEUTICAL HONG KONG LIMITE… | 有效 |

上表列出其中 5 張（共 49 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：骨質疏鬆、停經後骨質疏鬆、骨折、惡性貧血（此為圖譜關聯，並非仿單文字，臨床上多與長期使用 PPI 的骨質及維生素 B12 吸收風險有關）
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分範例：
  - **嚴重 (Major)**：Acalabrutinib、Atazanavir
  - **中度 (Moderate)**：Alpelisib、Amphotericin B、Atorvastatin、Bosutinib、Fenofibrate、Hydrochlorothiazide、Bumetanide 等
  - **輕微 (Minor)**：Acetylsalicylic acid、Cyanocobalamin、Axitinib、Bortezomib 等

其他警語與仿單禁忌症，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 活動性消化性潰瘍屬 Pantoprazole 的既有核心適應症，機轉明確，且有 Phase 3 試驗與多篇臨床文獻支持，香港含本藥成分的許可證皆為單一成分，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。
- 此項屬於「既有適應症確認」而非真正的新適應症，且仿單層級的安全性資料尚未取得。

<!-- review:begin hk-lic-20261117-pantoprazole-2 -->

> **查核更正（2026-11-24）**：原文為「活動性消化性潰瘍屬 Pantoprazole 的既有核心適應症，機轉明確，且有 Phase 3 試驗與多篇臨床文獻支持，同時香港已有 20 張有效許可證。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證皆為單一成分，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-pantoprazole-2 -->

**其他預測適應症概況：**

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 十二指腸阻塞 | 0.9921 | L5 | Hold；無明確機轉關聯，僅有一篇非評估 Pantoprazole 的病例報告 |

**若要推進需要：**
- 取得香港衛生署的仿單資料（警語、禁忌症、核准適應症），這是目前阻擋安全性篩查的缺口
- 補齊作用機轉（MOA）的正式資料
- 確認 NCT02084420 中 Pantoprazole 是試驗藥還是對照藥
- 針對長期使用的骨質疏鬆、骨折與維生素 B12 缺乏風險，建立監測計畫
- 評估與 Atazanavir、Acalabrutinib 等重大交互作用藥物併用時的處理原則

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「香港共有 20 張有效許可證，皆為單方製劑，目前無已註銷者。」→「香港含本藥成分的許可證皆為單一成分，張數與有效張數見本頁快速」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-24 | 「- 活動性消化性潰瘍屬 Pantoprazole 的既有核心適應症，機轉明確，且」→「- 活動性消化性潰瘍屬 Pantoprazole 的既有核心」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Protonix I.V. (pantoprazole sodium) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cde88e6-28f2-4cbe-8c3f-770b05cc0e1b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

