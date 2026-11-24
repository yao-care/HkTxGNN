---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 846
evidence_level: L5
indication_count: 8
monitor_inn: "TADALAFIL"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
last_modified_at: 2026-11-24
description: "Tadalafil：預測新適應症為Ambras 型先天性全身多毛症（證據等級 L5）。原適應症：知識圖譜記錄的關聯：良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛、早洩"
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Tadalafil：從勃起功能障礙等泌尿與肺部適應症到安布拉斯型全身性先天多毛症
{: .text-alpha }

## 一句話總結

Tadalafil 是一種 PDE5 抑制劑，知識圖譜中記錄的原有用途包括勃起功能障礙、良性前列腺增生與肺動脈高壓。
TxGNN 模型預測它可能對 **Ambras 型先天性全身多毛症 (Ambras type hypertrichosis universalis congenita)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：良性前列腺增生、肺動脈高壓、勃起功能障礙、心因性性交疼痛、早洩（香港許可證資料未提供適應症文字，無法以許可證確認） |
| 預測新適應症 | Ambras 型先天性全身多毛症 |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 54 張／共 55 張） |
| 許可證數 | 55 張（有效 54 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Tadalafil 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「性刺激期間之陰莖勃起，係由陰莖動脈及海綿體平滑肌鬆弛導致陰莖血流增加所引起。此反應係由神經末梢及內皮細胞釋放一氧化氮（NO）所媒介，NO 會刺激平滑肌細胞內 cGMP 之合成。[…] Tadalafil 會抑制 PDE5。」英文原文："Penile erection during sexual stimulation is caused by increased penile blood flow resulting from the relaxation of penile arteries and corpus cavernosal smooth muscle. This response is mediated by the release of nitric oxide (NO) from nerve terminals and endothelial cells, which stimulates the synthesis of cGMP in smooth muscle cells. […] Tadalafil inhibits PDE5."（[DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895)，版本日期 2026-06-03；查閱日期 2026-11-19）。已知 Tadalafil 屬於 PDE5 抑制劑，可提高細胞內 cGMP，作用於一氧化氮—cGMP 的血管舒張路徑。

Ambras 症候群是罕見的遺傳性毛髮發育異常，與染色體重組影響 TRPS1 調控有關。目前沒有已知的路徑能把 PDE5 抑制與此疾病連結。這個高分（0.9998）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性（如與其他多毛症條目的相似性），而非生物學證據，也不代表 Tadalafil 特有的機轉。

整體而言，此預測應視為純計算結果，合理性有限。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（補充：預測排名第 8 的「腦幹先兆偏頭痛」有一篇 2006 年個案報告 PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/)，指出 Tadalafil 與典型偏頭痛先兆相關，方向為可能誘發而非治療，且與本報告主要預測的疾病無關。）

---

## 香港上市資訊

以下為已列出的前 5 張許可證（共 55 張含本藥成分的許可證，有效 54 張、已註銷 1 張，皆為單一成分）。資料中未提供劑型與核准適應症文字。

<!-- review:begin hk-lic-20261117-tadalafil-1 -->

> **查核更正（2026-11-17）**：原文為「以下為已列出的前 5 張許可證（總數至少 20 張，清單可能不完整），均為單一成分製劑、狀態有效。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 55 張含本藥成分的許可證（有效 54 張、已註銷 1 張；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-tadalafil-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-68929 | CIATUFF 10 TABLETS 10MG | 單一成分 | AUROBINDO PHARMA LIMITED | 有效 |
| HK-65022 | ERETAF-20 TABLETS 20MG | 單一成分 | HOVID LIMITED | 有效 |
| HK-68281 | TADALAFIL AZEVEDOS TABLETS 20MG | 單一成分 | WA MAN (HK) LIMITED | 有效 |
| HK-66745 | DURACOR TABLETS 20MG | 單一成分 | SINO PACIFIC PHARMA COMPANY LIMITED | 有效 |
| HK-66950 | FIP TADALAFIL TABLETS 20MG | 單一成分 | WILSON TRADING COMPANY LIMITED | 有效 |

上表列出其中 5 張（共 55 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：肝衰竭、癲癇、主動脈瓣狹窄、低血壓、凝血疾病、急性冠心症、鐮狀細胞貧血、中風與腦血管疾病、心肌梗塞、血紅素病變、多發性骨髓瘤、陰莖異常勃起、Peyronie 病、聽力損失、白血病、肥厚型心肌病變等。
- **藥物交互作用**（共查得 100 筆，以下為部分中度交互作用）：Aprepitant、Dexamethasone、Lorcaserin、Canagliflozin、Cimetidine、Clarithromycin、Dapagliflozin、Empagliflozin、Sapropterin、Miconazole、Clotrimazole、Ertugliflozin、Troglitazone。
- **其他訊號**：Tadalafil 與偏頭痛先兆的個案報告顯示可能有神經血管方面的不良反應。

仿單的主要警語與禁忌資料未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病沒有任何臨床試驗或文獻支持，機轉上也缺乏合理連結，僅有模型分數。
- 其他預測中，「脊柱後側彎性心臟病」因肺高壓的間接關聯在生物學上相對合理，但同樣缺乏資料。多毛症方向甚至可能與血管擴張劑導致多毛的效果相反。

**若要推進需要：**
- 取得 Tadalafil 的作用機轉資料與香港仿單的警語、禁忌。
- 建立 PDE5/cGMP 與毛囊或 TRPS1 調控之間的機轉證據（體外或前臨床研究）。
- 系統性檢索該疾病的文獻與試驗，並確認作用方向（治療或誘發）。
- 若要探索替代方向，可優先評估與肺高壓相關的預測（如脊柱後側彎性心臟病），並評估缺氧性肺病中的通氣灌注風險。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「以下為已列出的前 5 張許可證（總數至少 20 張，清單可能不完整），均為單一成」→「以下為已列出的前 5 張許可證（共 55 張含本藥成分的許可」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Cialis (tadalafil) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bcd8f8ab-81a2-4891-83db-24a0b0e25895) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

