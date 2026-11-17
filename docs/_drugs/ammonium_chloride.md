---
layout: default
title: Ammonium Chloride
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 1
monitor_inn: "AMMONIUM CHLORIDE"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-31
description: "Ammonium Chloride：預測新適應症為鼻腔疾病（證據等級 L5）。原適應症：知識圖譜記錄的關聯：咽炎、感冒、鼻咽炎"
---

# Ammonium Chloride
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

## 氯化銨（Ammonium Chloride）：從咽炎、感冒到鼻腔疾病
{: .text-alpha }

## 一句話總結

氯化銨在知識圖譜中記錄的相關用途為咽炎、感冒與鼻咽炎，在香港則以祛痰類製劑形式上市。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：咽炎、感冒、鼻咽炎（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 鼻腔疾病 |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 169 張／共 170 張） |
| 許可證數 | 170 張（有效 169 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，氯化銨在香港多以祛痰劑、咳嗽糖漿等製劑上市，知識圖譜中也記錄了它與咽炎、感冒、鼻咽炎的關聯。

鼻腔疾病與上述上呼吸道病症在解剖位置和症狀上相近，模型可能因此給出高分。推測的作用方向是幫助稀釋或排出呼吸道分泌物，但這只是假設，沒有機轉或臨床資料可以佐證。

需要注意的是，此分數來自 TxGNN 模型（深度學習），很可能反映的是模型學到的鼻腔疾病與鼻咽炎、感冒等相關疾病之間的相似性，而不是生物學上的證據，也不是獨立的療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下為部分許可證（共 170 張含本藥成分的許可證，有效 169 張、已註銷 1 張，皆為複方）。品名為資料庫登記名稱，許可證資料未載明劑型與核准適應症文字。

<!-- review:begin hk-lic-20261117-ammonium_chloride-1 -->

> **查核更正（2026-11-17）**：原文為「以下為部分許可證（清單可能不完整，總數至少 20 張）。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 170 張含本藥成分的許可證（有效 169 張、已註銷 1 張；皆為複方）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-ammonium_chloride-1 -->

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-43251 | UNI-COPHEDENE SYRUP | Universal Pharmaceutical Laboratories, Limited |
| HK-07157 | UNI-PHEN EXPECTORANT | Universal Pharmaceutical Laboratories, Limited |
| HK-08384 | DIPHENAMINE EXPECTORANT | Vickmans Laboratories Ltd |
| HK-64814 | AXCEL FLEMIN EXPECTORANT SYRUP | Kotra Pharma (Hong Kong) Company |
| HK-54338 | BEANAMINE EXPECTORANT | Prudentlink Limited |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容，僅供參考）：高血壓、肝衰竭、癲癇、失眠、腎上腺皮質功能不全（含 Addison 病）、消化性潰瘍、良性前列腺增生、無尿、高血鈣、腎鈣化、磷代謝疾病、腎功能不全、高眼壓、心臟驟停、心臟傳導疾病、閉角型青光眼、甲狀腺功能亢進（含 Graves 病）、膀胱頸阻塞、肺水腫、心肌缺血、冠狀動脈疾病、焦慮症、強迫症、壞死性腸炎等。
- **藥物交互作用**：共查得 21 筆，其中中度交互作用為安非他命類藥物，包括 Amphetamine、Dextroamphetamine、Lisdexamfetamine、Metamfetamine、Benzphetamine。其餘多為輕度，涉及 Ephedrine、Pseudoephedrine、三環類抗憂鬱劑（如 Amitriptyline、Imipramine）、Methadone、Mexiletine、Flecainide 等。

仿單中的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但只有 TxGNN 模型（深度學習）的推論，沒有任何臨床試驗或文獻直接研究鼻腔疾病，證據等級為 L5。
- 作用機轉與仿單安全性資料均缺漏，目前無法評估可行性。

**若要推進需要：**
- 補齊作用機轉資料，驗證與鼻腔疾病的機轉關聯
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌
- 檢索並評估氯化銨用於鼻腔疾病的臨床或前臨床研究
- 明確定義鼻腔疾病的目標病況（如鼻塞、鼻竇炎），並評估劑型與給藥途徑是否適用

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「以下為部分許可證（清單可能不完整，總數至少 20 張）。」→「以下為部分許可證（共 170 張含本藥成分的許可證，有效 1」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

