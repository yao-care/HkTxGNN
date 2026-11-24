---
layout: default
title: Ambroxol
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Ambroxol：預測新適應症為鼻腔疾病 (Nasal Cavity Disease)（證據等級 L5）。原適應症：咽炎 (Pharyngitis)"
monitor_inn: "Ambroxol"
predicted_indications: ["nasal cavity disease", "vulvovaginal candidiasis", "faucial diphtheria", "cervical disc degenerative disorder"]
---

# Ambroxol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Ambroxol：從咽炎到鼻腔疾病
{: .text-alpha }

## 一句話總結

Ambroxol 是一種黏液溶解／袪痰藥物，原本用於咽炎（pharyngitis）。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇間接相關文獻**（急性咳嗽的綜述），證據仍屬早期。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 咽炎 (Pharyngitis) |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 45 張／共 45 張） |
| 許可證數 | 45 張（有效 45 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Ambroxol 是黏液溶解／分泌促進劑，可促進黏液纖毛清除並降低黏液黏稠度。另有報告指出它具有類局部麻醉（鈉通道阻斷）與抗發炎特性。

咽炎與鼻腔疾病同屬上呼吸道疾病，常伴隨黏液分泌異常，因此從機轉上看，改善黏液清除可能對鼻腔疾病有幫助。不過，這僅是間接推論，目前沒有針對鼻腔疾病的直接臨床證據。

此外，Ambroxol 作用於 GBA1（glucosylceramidase beta）的伴護蛋白（chaperone）活性，正被探索用於神經退化性疾病，但與鼻腔疾病無明確關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Review | Vestnik otorinolaringologii | 探討流感與急性呼吸道病毒感染相關急性咳嗽的治療新選擇；屬間接證據，未直接針對鼻腔疾病 |

## 香港上市資訊

香港共有 45 張含本藥成分的許可證（全部有效；皆為單一成分），以下列出 5 張主要許可證（資料中未載明劑型與核准適應症）：

<!-- review:begin hk-lic-20261117-ambroxol-1 -->

> **查核更正（2026-11-17）**：原文為「本藥在香港共有 20 張有效的單一成分許可證，以下列出 5 張主要許可證（資料中未載明劑型與核准適應症）：」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 45 張含本藥成分的許可證（全部有效；皆為單一成分）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-ambroxol-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-55459 | OBROXOL ORAL SOLUTION 30MG/10ML | 單一成分 | BRIGHT FUTURE PHARMACEUTICALS FACTORY O/B BRIGHT FUTURE PHARMACEUTICAL… | 有效 |
| HK-34878 | AMXOL TAB 30MG | 單一成分 | MEKIM LTD | 有效 |
| HK-61486 | UNION AMBROXOL TAB 30MG | 單一成分 | WAI LUN TRADING CO | 有效 |
| HK-46048 | AMBROXOL TAB 30MG | 單一成分 | CHRISTO PHARM LTD | 有效 |
| HK-44882 | AMBROXOL SR CAP 75MG (BRIGHT FUTURE) | 單一成分 | BRIGHT FUTURE PHARMACEUTICALS FACTORY O/B BRIGHT FUTURE PHARMACEUTICAL… | 有效 |

上表列出其中 5 張（共 45 張）。

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：資料庫查詢到 1 筆藥理學層面的交互作用，對象為 glucosylceramidase beta (GBA1)。Ambroxol 在細胞內（酸性溶酶體環境）可提高 GCase 酵素活性，在無細胞、中性 pH 環境下則呈抑制作用。此為藥理標靶資訊，未標示臨床嚴重程度。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數很高（0.9991），但沒有任何針對鼻腔疾病的臨床試驗，唯一文獻也只是急性咳嗽的間接綜述，證據等級僅 L4。
- 作用機轉只是合理推測，且缺乏仿單的警語與禁忌症資料，尚無法進行安全性篩選。

**若要推進需要：**
- 取得 Ambroxol 完整的作用機轉資料（MOA）
- 下載並解析香港衛生署的仿單，確認警語、禁忌症與核准適應症
- 針對鼻腔疾病（如鼻竇炎、鼻黏膜分泌過多）進行系統性文獻回顧
- 評估劑型與給藥途徑是否適合鼻腔疾病（目前路徑相容性尚未評估）
- 若文獻支持，再規劃小型探索性臨床試驗

**補充觀察：** 同批預測中，外陰陰道念珠菌病、白喉、頸椎椎間盤退化缺乏機轉與證據支持，建議維持 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本藥在香港共有 20 張有效的單一成分許可證，以下列出 5 張主要許可證（資料中」→「香港共有 45 張含本藥成分的許可證（全部有效；皆為單一成分」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

