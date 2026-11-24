---
layout: default
title: Phenazopyridine
parent: 僅模型預測 (L5)
nav_order: 686
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Phenazopyridine：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：資料中未載明核准適應症（泌尿道止痛用途為藥理分類推論）"
monitor_inn: "Phenazopyridine"
predicted_indications: ["bronchitis"]
---

# Phenazopyridine
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

## Phenazopyridine：從泌尿道不適到支氣管炎
{: .text-alpha }

## 一句話總結

Phenazopyridine 是一種泌尿道止痛藥，在香港為單方製劑，已有 12 張有效許可證。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，這僅是模型預測，且缺乏藥理學上的合理連結。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明核准適應症（泌尿道止痛用途為藥理分類推論） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 0.9923 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Phenazopyridine 一般被認為是泌尿道止痛劑，作用於泌尿道黏膜產生局部效果，但其確切機轉在本次彙整的資料中並未定義。

就現有資訊判斷，**並未建立可信的機轉連結**。Phenazopyridine 沒有已知的抗菌、抗發炎或支氣管擴張活性，無法解釋它如何改善氣道發炎或感染。泌尿道黏膜的局部止痛作用與支氣管炎的病理機制之間也沒有明顯關聯。

TxGNN 模型（深度學習）給出的高分（0.9923）可能反映模型從相關疾病之間學到的相似性，而非生物學證據。因此這個預測應謹慎看待。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本藥在香港的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。以下列出主要 5 張（資料中未提供劑型與核准適應症）：

<!-- review:begin hk-lic-20261124b-phenazopyridine-1 -->

> **查核更正（2026-11-24）**：原文為「本藥在香港共有 12 張有效單方許可證。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證包括單一成分與複方製劑；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-phenazopyridine-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-49457 | SURISHIA TAB 50MG | 單一成分 | HITPHARM PHARMACEUTICAL CO LTD | 有效 |
| HK-62852 | VICK-PYRIZO CAPSULES 100MG | 單一成分 | EUROPHARM LAB CO LTD | 有效 |
| HK-61946 | EURO-PHENAZO CAPSULES 100MG | 單一成分 | EUROPHARM LAB CO LTD | 有效 |
| HK-16853 | UROPRIN COATED TAB 100MG | 單一成分 | YUNG SHIN CO LTD | 有效 |
| HK-61945 | UNI-PENIDION CAPSULES 100MG | 單一成分 | EUROPHARM LAB CO LTD | 有效 |

上表列出其中 5 張（共 12 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自藥物－疾病關聯圖譜，非仿單內容，需以仿單核實）：
  - 肝臟：肝衰竭、肝病、肝性昏迷、肝性腦病變
  - 腎臟：腎臟疾病、輸尿管積膿
  - 血液：血液疾病、血小板低下、嗜中性白血球低下、顆粒球缺乏症、貧血（含巨球性貧血）
  - 代謝：遺傳性紫質症、紫質代謝疾病
  - 心血管與呼吸：高血壓、冠狀動脈疾病、慢性阻塞性肺病、睡眠呼吸中止症、先天性中樞性低通氣症候群
  - 其他：焦慮症、神經症、輕鬱症、物質濫用/依賴、良性攝護腺增生、膽囊疾病
- **藥物交互作用**：共查得 24 筆（以下為資料中列出的部分）
  - 重度：Nitrous acid、Leflunomide
  - 中度：Naltrexone、Methotrexate、局部麻醉藥類（Lidocaine、Benzocaine、Tetracaine、Cocaine 等）、Asparaginase、Brentuximab vedotin、Clofarabine、Idelalisib、Interferon beta-1a/1b、Pegaspargase

仿單警語與禁忌資料目前缺乏，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有任何臨床試驗或文獻，且機轉上找不到支持支氣管炎的藥理依據；TxGNN 模型（深度學習）的高分可能反映模型從相關疾病之間學到的相似性，而非生物學證據。
- 知識圖譜顯示多項潛在禁忌（含慢性阻塞性肺病、睡眠呼吸中止症等呼吸道相關疾病），對呼吸道適應症更需謹慎。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並評估與氣道發炎或感染是否有任何合理連結
- 取得香港衛生署仿單，確認原核准適應症、警語與禁忌
- 進行系統性文獻與試驗檢索，確認是否存在任何支持證據
- 確認給藥途徑相容性（目前尚待評估）
- 在上述條件未滿足前，不建議投入進一步開發資源

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「本藥在香港共有 12 張有效單方許可證。」→「本藥在香港的許可證包括單一成分與複方製劑，張數與有效張數見本」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

