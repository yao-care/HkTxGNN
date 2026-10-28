---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "Desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
description: "Desmopressin：預測新適應症為Congenital prothrombin deficiency（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Desmopressin
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

## Desmopressin: Congenital prothrombin deficiency
{: .text-alpha }

## 一句話總結

Desmopressin 原本用於遺傳性血管性血友病（von Willebrand disease）、血友病與夜間遺尿症。
TxGNN 模型的預測中，最值得進一步評估的是**原發性血小板釋放障礙 (Primary release disorder of platelets)**，
目前**無臨床試驗登記**，但有 **9 篇文獻**（含 1 篇 2023 年綜述、1 篇兒童世代研究）提供間接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Congenital prothrombin deficiency |
| TxGNN 預測分數 | 0.9970 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 14 張／共 14 張） |
| 許可證數 | 14 張（有效 14 張） |
| 建議決策 | Proceed with Guardrails |

> 說明：TxGNN 分數高低並不代表臨床價值。前 10 名預測中，只有「原發性血小板釋放障礙」達到 L3 並進入下一階段；其餘多為 Hold 或研究問題。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Desmopressin 是合成的血管加壓素類似物，透過 V2 受體促使內皮細胞釋放血管性血友病因子（VWF）與第八凝血因子（FVIII）。其在血管性血友病與輕度血友病 A 的療效已被證實，機轉上可能適用於部分血小板功能異常。

原發性血小板釋放障礙與儲存池缺陷屬於血小板功能異常。文獻顯示，Desmopressin 可提高 VWF 與 FVIII、增強血小板黏附與促凝活性，並縮短這類病人的出血時間。一項兒童研究評估了其對阿斯匹靈樣缺陷（遺傳性血小板病變）初級止血的影響。2023 年的綜述也整理了它作為止血與節血藥物的角色。

但證據多為小型或觀察性研究，個體反應不一，確切機轉仍有爭議（VWF/FVIII 濃縮製劑對此類疾病無效，顯示作用不僅止於 VWF 上升）。因此建議以試驗性輸注確認反應並加強監測。

### 其他預測的簡要評估

| 預測疾病 | TxGNN 分數 | 證據等級 | 評估 |
|---------|-----------|---------|------|
| 先天性凝血酶原缺乏症 | 0.9970 | L5 | 機轉連結薄弱，Desmopressin 不影響凝血酶原；高分可能反映網路鄰近性。Hold |
| 遺傳性血栓傾向 | 0.9944 | L5 | 促血栓狀態，與止血藥機轉相悖；文獻僅有與遺傳性 TTP 相關的病例報告，可能為偽陽性並帶有安全訊號。Hold |
| Glanzmann 血小板無力症 | 0.9930 | L4 | 無法修正缺失的 αIIbβ3 受體；僅有間接證據，標準治療為血小板輸注、rFVIIa 與抗纖溶藥。列為研究問題 |
| Scott 症候群 | 0.9916 | L5 | 缺陷在磷脂醯絲胺酸暴露，Desmopressin 無直接作用。列為研究問題 |
| 「flood factor deficiency」 | 0.9915 | L5 | 疾病名稱疑似來源資料錯置，僅連結到一般 VWD 綜述；需先確認疾病對應。列為研究問題 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為原發性血小板釋放障礙相關文獻（依類型與相關性挑選）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Review | Eur J Haematol | Desmopressin 可釋放 VWF 與 FVIII、增強血小板黏附並縮短出血時間，可用於輕度血友病 A、特定 VWD 亞型及尿毒症與肝病出血；須留意低血鈉及罕見動脈血栓事件 |
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Cohort | Klin Padiatr | 評估兒童阿斯匹靈樣缺陷（遺傳性血小板病變）使用 Desmopressin 後對初級止血的影響 |
| [23051555](https://pubmed.ncbi.nlm.nih.gov/23051555/) | 2013 | Cohort | Haemophilia | 輸注 Desmopressin 後，與微粒結合的 VWF 增加，可能解釋其對血小板疾病的作用 |
| [22057877](https://pubmed.ncbi.nlm.nih.gov/22057877/) | 2011 | Case report | Hamostaseologie | Hermansky-Pudlak 症候群（δ 顆粒釋放缺陷）以難治性月經過多為首發表現 |
| [22726100](https://pubmed.ncbi.nlm.nih.gov/22726100/) | 2012 | Review | Haemophilia | 遺傳性血小板疾病總覽，涵蓋分泌與儲存缺陷 |
| [18278172](https://pubmed.ncbi.nlm.nih.gov/18278172/) | 2008 | Review | Thromb Haemost | 先天性血小板功能異常的分類與表現 |
| [16580053](https://pubmed.ncbi.nlm.nih.gov/16580053/) | 2006 | Review | Thromb Res | VWD 預防性治療；Desmopressin 為多數病人的主要治療 |
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Review | Gastroenterology | AGA 肝硬化凝血臨床實務更新（間接相關） |
| [34818873](https://pubmed.ncbi.nlm.nih.gov/34818873/) | 2022 | RCT | Haematologica | VWF A1 結構域適體 BT200 的首次人體試驗，與 Desmopressin 無直接關聯 |

---

## 香港上市資訊

香港共有 14 張有效許可證，皆為單方製劑，無已註銷者；資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37371 | MINIRIN TAB 0.1MG（Ferring） | 錠劑 | 未載明 |
| HK-37370 | MINIRIN TAB 0.2MG（Ferring） | 錠劑 | 未載明 |
| HK-54452 | MINIRIN MELT ORAL LYOPHILISATE 60MCG（Ferring） | 口溶凍晶劑 | 未載明 |
| HK-32872 | MINIRIN INJ 4MCG/ML（Ferring） | 注射劑 | 未載明 |
| HK-38155 | OCTOSTIM INJ 15UG/ML（Ferring） | 注射劑 | 未載明 |

其餘 9 張包括 NURITAN、MINIS、PMS-DESMOPRESSIN、NOCDURNA 與 MINIRIN MELT 120MCG 等不同規格與廠牌。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**：高血壓、冠狀動脈疾病、腎功能不全、囊性纖維化、呼吸道感染、過敏性與血管運動性鼻炎、原發性多飲／渴感性尿崩症、水中毒、血管性血友病（特定亞型）。此為知識圖譜關聯，並非仿單文字。
- **血栓與血小板相關訊號**：病例報告顯示 Desmopressin 可誘發或惡化血栓性血小板低下紫斑症（TTP）；對 VWD 2B 型可能造成血小板低下。凡有 TTP、血栓傾向或血小板型 VWD 者，應避免使用。
- **低血鈉**：文獻綜述指出使用可能併發低血鈉。
- **藥物交互作用**：已查得 100 筆，以下為主要項目：
  - 重大（Major）：Hydrocortisone、Triamcinolone、Dexamethasone、Beclomethasone、Betamethasone、Budesonide、Prednisolone、Prednisone
  - 中度（Moderate）：Epinephrine、Loperamide、Morphine、Opium、Chlorpropamide
  - 輕微（Minor）：Acetylsalicylic acid

仿單的警語與禁忌資料尚未取得，其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限原發性血小板釋放障礙）

**理由：**
- 此適應症有機轉合理性，並有綜述、兒童世代與機轉研究的間接支持（L3），但無臨床試驗，且反應存在個體差異。
- 其他預測多為機轉薄弱、證據不足，或有明確負面安全訊號（TTP、血栓傾向、血小板型 VWD），建議 Hold 或僅列為研究問題。

**若要推進需要：**
- 取得香港仿單的警語與禁忌，並補齊作用機轉資料
- 設計前瞻性小型試驗或登錄研究，以出血時間、血小板功能與 VWF/FVIII 為指標
- 訂定使用護欄：先做試驗性輸注確認反應、監測血鈉與血小板計數，排除 TTP、血栓傾向與 2B 型 VWD
- 釐清「flood factor deficiency」的疾病對應是否為資料錯置
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

